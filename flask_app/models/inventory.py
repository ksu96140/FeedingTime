from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash, session

class Inventory:
    db = 'feeding_time_schema'
    def __init__(self, data):
        self.id = data['id']
        self.gold = data['gold']
        self.carrot = data['carrot']
        self.apple = data['apple']
        self.rice = data['rice']
        self.cheese = data['cheese']
        self.fish = data['fish']
        self.chicken = data['chicken']
        self.blueberry = data['blueberry']
        self.popcorn = data['popcorn']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        
    #create inventory
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO inventories (gold, carrot, apple, rice, cheese, fish, chicken, blueberry, popcorn, user_id) VALUES (100, 0, 0, 0, 0, 0, 0, 0, 0, %(user_id)s)'
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get inventory
    @classmethod
    def view(cls, data):
        query = "SELECT * FROM inventories WHERE user_id=%(user_id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    #update inventory
    @classmethod
    def update(cls, data):
        query = "UPDATE inventories SET carrot=carrot+%(carrot)s, apple=apple+%(apple)s, rice=rice+%(rice)s, cheese=cheese+%(cheese)s, fish=fish+%(fish)s, chicken=chicken+%(chicken)s, blueberry=blueberry+%(blueberry)s, popcorn=popcorn+%(popcorn)s WHERE user_id=%(user_id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #check gold
    @classmethod
    def gold(cls, data):
        query = "SELECT gold FROM inventories WHERE user_id=%(user_id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result[0]['gold']

    #calculate gold & update db
    @classmethod
    def update_gold(cls, data):
        query = "UPDATE inventories SET gold=%(gold)s WHERE user_id=%(user_id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #purchase validation
    @staticmethod
    def purchase_valid(purchase):
        is_valid = True
        carrot = purchase['carrot'] * 5
        apple = purchase['apple'] * 9
        rice = purchase['rice'] * 8
        cheese = purchase['cheese'] * 7
        fish = purchase['fish'] * 15
        chicken = purchase['chicken'] * 12
        blueberry = purchase['blueberry'] * 3
        popcorn = purchase['popcorn'] * 1
        gold = purchase['gold']
        session['cartSum'] = carrot + apple + rice + cheese + fish + chicken + blueberry + popcorn
        if session['cartSum'] > gold:
            flash("You don't have enough gold!")
            is_valid = False
            session.pop('cartSum')
        return is_valid
    