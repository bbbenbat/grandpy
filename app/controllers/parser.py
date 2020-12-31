"""
This module allows you to manage the processing of a sentence in order to
find the keywords for internet research.
"""
import json
import re
import string


class Checkdata:
    """ this class contains several methods which allow
    you to find the keywords of a sentence.  """

    def low_case(self, req):
        """ Change all caracters in low-case. """
        return req.lower()

    def delete_punctuation(self, req):
        """ Replace all punctuation by whitespace. """
        replace_punctuation = str.maketrans(
            string.punctuation, ' ' * len(string.punctuation))
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
        path_json = '/'
        clean_list = []
        result = ""
        with open('app/models/fr.json') as f:
            data = json.load(f)
        data = data['key_words']
        for var in req:
            for var2 in data:
                if str(var) == str(var2):
                    clean_list.append(var)
            if var not in clean_list:
                result += var + ' '
        return result

    def parser_complet(self, req):
        """ Use all methods from the Class to parse 'req'. """
        req = self.low_case(req)
        req = self.delete_punctuation(req)
        req = self.create_list(req)
        req = self.find_word(req)
        return req
