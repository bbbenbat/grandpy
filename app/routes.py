""" This module manages the routes of the website.
 It gives a link between an url and a html page.
 It can give arguments to the pages."""
import os

from flask import render_template, request, jsonify

from app import app
from app.controllers import parser
from app.models import google_api
from app.models import wikipedia_api


@app.route('/', methods=['GET', 'POST'])
def index():
    # Return the html page with an argument.
    google_api_k = os.getenv('GOOGLE_API_KEY')
    return render_template('index.html', title='GrandPyBot',
                           google_api_k=google_api_k)


@app.route('/tempo', methods=['GET', 'POST'])
def tempo():
    # val_check is a variable to check the return of methods
    val_check = 0
    # save the question into variable
    req = request.args.get('question')
    # call the parser
    parser_ob = parser.Checkdata()
    pars_result = parser_ob.parser_complet(req)
    if pars_result == 0:
        val_check = 1
    else:
        # call googlemaps api for research on 'req'
        google_ob = google_api.GoogleApi()
        google_result = google_ob.run(pars_result)
        if google_result == 0:
            val_check = 1
        else:
            address = google_result[0]
            latitude = google_result[1]
            longitude = google_result[2]
            # wiki result
            wiki_api = wikipedia_api.WikiApi(latitude, longitude)
            wiki_result = wiki_api.resum_result()
            if wiki_result == 0:
                val_check = 1
    if val_check == 1:
        return jsonify({'val': val_check})
    else:
        title = wiki_result[0]
        resume = wiki_result[1]
        return jsonify({'val': val_check, 'title': title,
                        'address': address, 'resume': resume,
                        'latitude': latitude, 'longitude': longitude})
