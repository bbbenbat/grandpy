""" This module establishes a connection to the wikipedia API in order
to retrieve information on the address sought. """

import time

import wikipedia


class WikiApi:
    """ This class is used to establish a connection to the wikipedia
    API and return a description of the address sought. """

    def __init__(self, latitude, longitude):
        wikipedia.set_lang("fr")
        self.latitude = latitude
        self.longitude = longitude

    def loc_result(self):
        """ Find the location name by these coordinates. """
        question = (wikipedia.geosearch(
            self.latitude, self.longitude, results=1))
        return question

    def resum_result(self):
        """ Return 2 sentences describing the place.  """
        question = self.loc_result()
        if question == []:
            return 0
        else:
            title = question[0]
            resume = wikipedia.summary(title, sentences=2)
            time.sleep(2)
            return title, resume
