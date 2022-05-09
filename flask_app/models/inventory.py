from flask_app.config.mysqlconnection import connectToMySQL

class Inventory:
    db = 'feeding_time_schema'
    def __init__(self, data):
        self.id = data['id']
        self.gold = 100
        self.carrot = 0
        self.apple = 0
        self.rice = 0
        self.cheese = 0
        self.fish = 0
        self.blueberry = 0
        self.popcorn = 0
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        
    #create inventory
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO inventories (user_id) VALUES (%(user_id)s)'
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get inventory
    @classmethod
    def view(cls, data):
        query = "SELECT * FROM inventories WHERE user_id=%(user_id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #update inventory
    @classmethod
    def update(cls, data):
        query = "UPDATE inventories SET gold=%(gold)s, carrot=%(carrot)s, apple=%(apple)s, rice=%(rice)s, cheese=%(cheese)s, fish=%(fish)s, blueberry=%(blueberry)s, popcorn=%(popcorn)s WHERE user_id=%(user_id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    
