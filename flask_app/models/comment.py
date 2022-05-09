from flask_app.config.mysqlconnection import connectToMySQL

class Comment:
    db = 'feeding_time_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    #create comment
    @classmethod
    def comment(cls, data):
        query = "INSERT INTO comments (name, comment, user_id) VALUES (%(name)s, %(comment)s, %(user_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get all comments for user
    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM comments WHERE user_id=%(user_id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get single comment
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM comments WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #update comment
    @classmethod
    def update(cls, data):
        query = "UPDATE comments SET comment=%(comment)s WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #delete comment
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM comments WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    