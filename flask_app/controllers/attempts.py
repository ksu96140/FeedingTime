from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app

@app.route('/start')
def startFeeding():
    return render_template('mocha.html')

@app.route('/end')
def endFeeding():
    return render_template('results.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')