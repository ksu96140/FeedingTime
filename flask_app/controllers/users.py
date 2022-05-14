from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.attempt import Attempt
from flask_app.models.comment import Comment
from flask_app.models.inventory import Inventory
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validation(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['fname'],
        'last_name' : request.form['lname'],
        'birthday' : request.form['birthday'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    User.create(data)
    user_in_db = User.get_user(data)
    session['user_id'] = user_in_db.id
    session['user_name'] = user_in_db.first_name
    return redirect('/score')

@app.route('/login', methods=['POST'])
def login():
    data = { 'email' : request.form['email'] }
    user_in_db = User.get_user(data)
    if not user_in_db:
        flash("Invalid email or password!", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid email or password!", "login")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['user_name'] = user_in_db.first_name
    return redirect('/score')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/score')
def homepage():
    if 'attempt' in session:
        session.pop('attempt')
    if 'inventory' in session:
        session.pop('inventory')
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id': session['user_id'],
    }
    all_attempts = Attempt.get_user_attempts(data)
    all_comments = Comment.get_all(data)
    return render_template('score.html', attempts=all_attempts, comments=all_comments)

#view other players
@app.route('/score/<int:user_id>')
def view_page(user_id):
    data = {
        'user_id' : user_id
    }
    user_data = User.view_player(data)
    all_attempts = Attempt.get_user_attempts(data)
    all_comments = Comment.get_all(data)
    print(User.view_player(data).first_name)
    return render_template('view_player.html', user=user_data, attempts=all_attempts, comments=all_comments)