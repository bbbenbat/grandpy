""" This module checks that all the methods of the parser are working. """

from app.controllers import parser

pars = parser.Checkdata()

# CONSTANTS
QUESTION = "Salut GrandPy, comment vas-tu? " \
           "Peux-tu me dire où se trouve l'Arc de Triomphe?"


def test_low_case():
    """ Test low_case method from Checkdata Class. """
    req = pars.low_case(QUESTION)
    result = QUESTION.lower()
    assert req == result


def test_delete_punctuation():
    """ Test delete_punctuation method from Checkdata Class. """
    req = pars.delete_punctuation(QUESTION)
    result = "Salut GrandPy comment vas tu Peux tu me dire où " \
             "se trouve l Arc de Triomphe "
    assert req == result


def test_create_list():
    """ Test create_list method from Checkdata Class. """
    question = "Salut GrandPy comment vas tu Peux " \
               "tu me dire où se trouve l Arc de Triomphe "
    req = pars.create_list(question)
    result = ['Salut', 'GrandPy', 'comment', 'vas', 'tu', 'Peux',
              'tu', 'me', 'dire', 'où', 'se', 'trouve', 'l', 'Arc',
              'de', 'Triomphe']
    assert req == result


def test_find_word():
    """ Test find_word method for Checkdata Class. """
    question = ['salut', 'grandpy', 'comment', 'vas', 'tu',
                'peux', 'tu', 'me', 'dire', 'où', 'se', 'trouve',
                'l', 'arc', 'de', 'triomphe']
    req = pars.find_word(question)
    result = "où trouve arc triomphe "
    assert str(req) == str(result)
