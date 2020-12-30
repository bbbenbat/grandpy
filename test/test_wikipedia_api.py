""" This module checks that the WikiApi methods work correctly. """

from app.models import wikipedia_api

# CONSTANTS
LATITUDE = 48.85837009999999
LONGITUDE = 2.2944813
WIKI_RES = ['Tour Eiffel']

wiki_api = wikipedia_api.WikiApi(LATITUDE, LONGITUDE)


def test_wikiapi_loc_result():
    """ Test that the method returns the correct result. """
    req = wiki_api.loc_result()
    result = WIKI_RES
    assert req == result


def mock_wikiapi_loc_result(self):
    """ Mock the method 'loc_result' to replace it in the next test. """
    result = WIKI_RES
    return result


def test_wikiapi_resum_result(monkeypatch):
    """ Test the method 'resum_result' with
    the patching of 'mock_wikiapi_loc_result'. """
    monkeypatch.setattr(
        'app.models.wikipedia_api.WikiApi.loc_result', mock_wikiapi_loc_result)
    req = wiki_api.resum_result()
    result = ('Tour Eiffel',
              'La tour Eiffel  est une tour de fer puddlé de 324 mètres de '
              'hauteur (avec antennes) située à Paris, '
              'à l’extrémité nord-ouest '
              'du parc du Champ-de-Mars en bordure '
              'de la Seine dans le 7e arrondissement. '
              'Son adresse officielle est 5, avenue Anatole-France.')
    assert req == result
