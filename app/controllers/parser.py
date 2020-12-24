"""

"""
import json
import re
import string


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
        """ Transform string (without punctuation) into a list. """
        list = []
        for word in req.split():
            list.append(word)
        return list

    def find_word(self, req):
        """ Clean the string with keyword. """
        path_json = 'D:/OCR/P7 - GrandPy/grandpy/app/models/fr.json'
        clean_list = []
        result = ""
        with open(path_json) as f:
            data = json.load(f)
        data = data['key_words']
        for var in req:
            for var2 in data:
                if str(var) == str(var2):
                    clean_list.append(var)
            if var not in clean_list:
                result += var + ' '
        return result




