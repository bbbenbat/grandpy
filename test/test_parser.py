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
    """  """
    req = pars.low_case(QUESTION)
    result = QUESTION.lower()
    assert req == result

def test_delete_punctuation():
    """  """
    req = pars.delete_punctuation(QUESTION)
    result = "Salut GrandPy comment vas tu Peux tu me dire où se trouve l Arc de Triomphe "
    assert req == result

"""def test_check_data_question():
    """  """

    result = "Arc de triomphe"
    ret = pars.check_word(QUESTION)
    result == ret"""

