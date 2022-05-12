from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
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
    session['user_fullname'] = user_in_db.first_name + ' ' + user_in_db.last_name
    return redirect('/dashboard')

@app.route('/score')
def success():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('score.html')