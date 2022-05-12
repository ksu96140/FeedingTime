from flask_app import app
from flask_app.controllers import inventories, users, attempts, comments

if __name__=='__main__':
    app.run(debug=True)