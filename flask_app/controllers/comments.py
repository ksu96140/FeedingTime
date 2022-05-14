from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.comment import Comment

#post a comment
@app.route('/comment', methods=['POST'])
def comment():
    data = {
        'user_id' : request.form['user_id'],
        'commenter_id' : session['user_id'],
        'name' : request.form['name'],
        'comment' : request.form['comment']
    }
    Comment.comment(data)
    return redirect('/leaderboard')

#delete this comment
@app.route('/delete_comment', methods=['POST'])
def delete():
    data = {
        'id' : request.form['id']
    }
    Comment.delete(data)
    return redirect('/score')

#edit this comment
@app.route('/edit_comment', methods=['POST'])
def edit():
    data = {
        'id' : request.form['id'],
        'comment' : request.form['comment']
    }
    user_id = request.form['user_id']
    Comment.update(data)
    return redirect(f'/score/{user_id}')