""" This module tests all the methods of the GoogleMaps_api module. """
from app.models import google_api

google_map = google_api.GoogleApi()

# CONSTANTS
QUESTION = 'tour eiffel'
GOOGLE_RES = [{'address_components': [
    {'long_name': '5', 'short_name': '5', 'types': ['street_number']},
    {'long_name': 'Avenue Anatole France',
     'short_name': 'Avenue Anatole France',
     'types': ['route']},
    {'long_name': 'Paris', 'short_name': 'Paris',
     'types': ['locality', 'political']},
    {'long_name': 'Département de Paris',
     'short_name': 'Département de Paris',
     'types': ['administrative_area_level_2', 'political']},
    {'long_name': 'Île-de-France', 'short_name': 'IDF',
     'types': ['administrative_area_level_1', 'political']},
    {'long_name': 'France', 'short_name': 'FR',
     'types': ['country', 'political']},
    {'long_name': '75007',
     'short_name': '75007',
     'types': ['postal_code']}],
    'formatted_address':
        'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
    'geometry': {'location': {'lat': 48.85837009999999, 'lng': 2.2944813},
                 'location_type': 'ROOFTOP',
                 'viewport':
                     {'northeast': {'lat': 48.8597190802915,
                                    'lng': 2.295830280291502},
                      'southwest':
                          {'lat': 48.8570211197085,
                           'lng': 2.293132319708498}}
                 },
    'place_id': 'ChIJLU7jZClu5kcR4PcOOO6p3I0',
    'plus_code': {'compound_code': 'V75V+8Q Paris, France',
                  'global_code': '8FW4V75V+8Q'},
    'types': ['establishment',
              'point_of_interest', 'tourist_attraction']
}]


def test_googleApi_run_api():
    """ Test whether the function returns the correct information. """
    req = google_map.run_api(QUESTION)
    result = GOOGLE_RES
    assert result == req


def mock_googleapi_run_api(self, req):
    """ Mock the methode 'run_api' to replace it in the next test. """
    result = GOOGLE_RES
    return result


def test_googleApi_run(monkeypatch):
    """ Test the method 'run' with the patching of 'mock_googleapi_run_api'."""
    monkeypatch.setattr('app.models.google_api.GoogleApi.run_api',
                        mock_googleapi_run_api)
    req = google_map.run(QUESTION)
    result = ('Champ de Mars, '
              '5 Avenue Anatole France, '
              '75007 Paris, '
              'France', 48.85837009999999, 2.2944813)
    assert result == req
