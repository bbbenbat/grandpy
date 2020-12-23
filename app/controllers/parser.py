"""

"""
import string
import re

class Checkdata:
    """  """
    def __init__(self):
        pass


    def low_case(self, req):
        """ Change all caracters in low-case. """
        return req.lower()

    def delete_punctuation(self, req):
        """ Replace all punctuation by whitespace. """
        replace_punctuation = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        text = req.translate(replace_punctuation)
        text = re.sub(' +', ' ', text)
        return text

    def create_list(self, req):
        """ Transform string by a list. """
        return req

def check_word(self, req):
        """
        mettre les mots dans une liste avec un split par les espaces
        application du filtre
        """
        return req

a = Checkdata()
a.create_list("Salut GrandPy comment vas tu Peux tu me dire où se trouve l Arc de Triomphe ")