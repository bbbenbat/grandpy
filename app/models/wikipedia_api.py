"""  """

import time

import wikipedia


class WikiApi:
    """  """

    def __init__(self, latitude, longitude):
        wikipedia.set_lang("fr")
        self.latitude = latitude
        self.longitude = longitude

    def loc_result(self):
        """ Find the location name by these coordinates. """
        question = (wikipedia.geosearch(self.latitude, self.longitude, results=1))
        return question

    def resum_result(self):
        """ Return 3 sentences describing the place.  """
        question = self.loc_result()
        title = question[0]
        resume = wikipedia.summary(title, sentences=2)
        time.sleep(2)
        return title, resume
