from flask import render_template, flash, redirect

from app import app
from app.forms import SendMessage


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SendMessage()
    user = {'username': 'Mon poussin'}
    user2 = {'username': 'GrandPy'}
    posts = [
        {
            'author': {'username': user['username']},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': user2['username']},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    if form.validate_on_submit():
        flash('Text requested for message {}'.format(
            form.message.data))
        return redirect('/')
    return render_template('index.html', title='GrandPyBot', user=user, posts=posts, form=form)
