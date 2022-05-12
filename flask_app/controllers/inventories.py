from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app

@app.route('/shop')
def shop():
    return render_template('shop.html')