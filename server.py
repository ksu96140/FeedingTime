from flask_app import app
from flask_app.controllers import inventories, users, attempts

if __name__=='__main__':
    app.run(debug=True)