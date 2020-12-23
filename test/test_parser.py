"""

"""

from app.controllers import parser


# Soit ...
# Quand... j'accompli une action
# Alors... je constate que

pars = parser.Checkdata()
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
    result = "Salut GrandPy comment vas tu Peux tu me dire où se trouve l Arc de Triomphe "
    assert req == result

def test_create_list():
    """ Test create_list method from Checkdata Class. """
    req = pars.create_list(QUESTION)
    result = ['Salut', 'GrandPy', 'comment', 'vas', 'tu', 'Peux', 'tu', 'me', 'dire', 'où', 'se', 'trouve', 'l', 'Arc', 'de', 'Triomphe']
    assert req == result

"""def test_check_data_question():
    """  """

    result = "Arc de triomphe"
    ret = pars.check_word(QUESTION)
    result == ret"""

