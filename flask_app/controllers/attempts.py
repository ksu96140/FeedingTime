from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.inventory import Inventory
from flask_app.models.attempt import Attempt

@app.route('/start')
def startFeeding():
    data = {
        'user_id' : session['user_id']
    }
    session['attempt'] = Attempt.create(data)
    return render_template('mocha.html', inventory=Inventory.view(data))

#feed mocha
@app.route('/feed', methods=['POST'])
def feed():
    data = {
        'user_id' : session['user_id'],
        'carrot' : int(request.form['carrot']),
        'apple' : int(request.form['apple']),
        'rice' : int(request.form['rice']),
        'cheese' : int(request.form['cheese']),
        'fish' : int(request.form['fish']),
        'chicken' : int(request.form['chicken']),
        'blueberry' : int(request.form['blueberry']),
        'popcorn' : int(request.form['popcorn']),
    }
    updateAttempt = {
        'id' : session['attempt'],
        'score' : Attempt.score(data)
    }
    Attempt.update_score(updateAttempt)
    session['score'] = Attempt.score(data)
    return redirect('/end')

@app.route('/end')
def endFeeding():
    return render_template('results.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')