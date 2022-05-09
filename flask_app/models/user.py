from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash
from datetime import datetime, date
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class User:
    db = 'feeding_time_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.birthday = data['birthday']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #create user
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO users (first_name, last_name, birthday, email, password) VALUES (%(first_name)s, %(last_name)s, %(birthday)s, %(email)s, %(password)s)'
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get user info
    @classmethod
    def get_user(cls, data):
        query = 'SELECT * FROM users WHERE email=%(email)s'
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    #registration validation
    @staticmethod
    def validation(user):
        is_valid = True
        if User.get_user(user):
            flash("User already exists!", "register")
            is_valid = False
        first_name = user['fname']
        last_name = user['lname']
        if (len(first_name)<2) or (len(last_name)<2):
            flash("Names must be at least 2 characters long", "register")
            is_valid = False
        if not ((first_name.isalpha()) or (last_name.isalpha())):
            flash("Names must all be letters", "register")
            is_valid = False
        if user['birthday']=="":
            flash("Please enter your birthday", "register")
            is_valid = False
        else:
            birthday = datetime.strptime(user['birthday'], "%Y-%m-%d")
            today = date.today()
            if (today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))) < 9:
                flash("Must be over 8 years old to register", "register")
                is_valid = False
        if not len(user['email'])>0:
            flash("Please enter email", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address", "register")
            is_valid = False
        if not PASSWORD_REGEX.match(user['password']):
            flash("Password must be at least 8 characters long, containing at least 1 uppercase letter, 1 lowercase letter, and 1 number", "register")
            is_valid = False
        if user['password'] != user['cPassword']:
            flash("Please check for typos in password", "register")
            is_valid = False
        return is_valid