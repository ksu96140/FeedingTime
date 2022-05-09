from flask_app.config.mysqlconnection import connectToMySQL

class Attempt:
    db = 'feeding_time_schema'
    def __init__(self, data):
        self.id = data['id']
        self.score = data['score']
        self.like = data['like']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    #create attempt
    @classmethod
    def create(cls, data):
        query = "INSERT INTO attempts (score, like) VALUES (%(score)s, '0')"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #update score
    @classmethod
    def update_score(cls, data):
        query = "UPDATE attempts SET score=%(score)s WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #update likes
    @classmethod
    def update_like(cls, data):
        query = "UPDATE attempts SET like=%(like)s WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)