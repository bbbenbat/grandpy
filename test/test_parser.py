"""

"""

from app.controllers import parser


# Soit ...
# Quand... j'accompli une action
# Alors... je constate que


def test_check_data_question():
    """  """
    pars = parser.Checkdata()
    question = "Salut GrandPy, comment vas-tu? " \
               "Peux-tu me dire où se trouve l\'Arc de Triomphe?"
    result = "Arc de triomphe"
    ret = pars.check_word(question)
    assert result == ret

