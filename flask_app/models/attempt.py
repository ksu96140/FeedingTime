from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash, session

class Attempt:
    db = 'feeding_time_schema'
    def __init__(self, data):
        self.id = data['id']
        self.score = data['score']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    #create attempt
    @classmethod
    def create(cls, data):
        query = "INSERT INTO attempts (score, user_id) VALUES (0, %(user_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get attempt
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM attempts WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get top 10 attempts
    @classmethod
    def get_user_attempts(cls, data):
        query = "SELECT * FROM attempts WHERE user_id=%(user_id)s ORDER BY score desc LIMIT 10"
        return connectToMySQL(cls.db).query_db(query, data)

    #get best attempt of all users
    @classmethod
    def best_attempt(cls):
        query = "SELECT MAX(score), attempts.updated_at, users.first_name, users.last_name, user_id FROM attempts JOIN users ON attempts.user_id=users.id GROUP BY user_id ORDER BY MAX(score) desc"
        return connectToMySQL(cls.db).query_db(query)
    
    #update score
    @classmethod
    def update_score(cls, data):
        query = "UPDATE attempts SET score=%(score)s WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #update likes
    @classmethod
    def update_like(cls, data):
        query = "UPDATE attempts SET likes=%(likes)s WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #calculate score
    @staticmethod
    def score(data):
        carrot = data['carrot'] * 10
        apple = data['apple'] * 15
        rice =data['rice'] * 5
        cheese = data['cheese'] * 2
        fish = data['fish'] * 15
        chicken = data['chicken'] * 20
        blueberry = data['blueberry'] * 6
        popcorn = data['popcorn'] * 1
        sum = carrot + apple + rice + cheese + fish + chicken + blueberry + popcorn
        return sum