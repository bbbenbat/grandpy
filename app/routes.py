from flask import render_template, flash, redirect, jsonify, request

from app import app



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='GrandPyBot')


@app.route('/toto', methods=['GET', 'POST'])
def toto():
    req = request.args.get('question')

    val="voici ce que j'ai trouvé"+req

    return render_template('toto.html', val=val)
