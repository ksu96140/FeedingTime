from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.inventory import Inventory
from flask_app.models.attempt import Attempt

@app.route('/start')
def startFeeding():
    if 'inventory' not in session:
        return redirect('/score')
    data = {
        'user_id' : session['user_id'],
        'id' : session['inventory']
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
    if 'user_id' not in session:
        return redirect('/')
    if 'inventory' not in session:
        return redirect('/score')
    if 'attempt' not in session:
        return redirect('/score')
    session.pop('inventory')
    session.pop('gold')
    return render_template('results.html')

@app.route('/leaderboard')
def leaderboard():
    if 'user_id' not in session:
        return redirect('/')
    if 'player_id' in session:
        session.pop('player_id')
    if 'gold' in session:
        session.pop('gold')
    if 'score' in session:
        session.pop('score')
    return render_template('leaderboard.html', leaderboard=Attempt.best_attempt())