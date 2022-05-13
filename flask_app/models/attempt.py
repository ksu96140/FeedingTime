from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash, session

class Attempt:
    db = 'feeding_time_schema'
    def __init__(self, data):
        self.id = data['id']
        self.score = data['score']
        self.likes = data['likes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    #create attempt
    @classmethod
    def create(cls, data):
        query = "INSERT INTO attempts (score, likes, user_id) VALUES (0, 0, %(user_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get attempt
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM attempts WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get all attempts
    @classmethod
    def get_user_attempts(cls, data):
        query = "SELECT * FROM attempts WHERE user_id=%(user_id)s"
        return connectToMySQL(cls.db).query_db(query, data)

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
        fish = data['fish'] * 8
        chicken = data['chicken'] * 14
        blueberry = data['blueberry'] * 6
        popcorn = data['popcorn'] * 1
        sum = carrot + apple + rice + cheese + fish + chicken + blueberry + popcorn
        return sum