""" This module allows you to manage the Google Maps API in order to find
the coordinates of a variable (the keywords found). """
import os
import time

import googlemaps

GOOGLE_KEY = os.getenv('GOOGLE_API_KEY')


class GoogleApi:
    """ This class is used to establish a connection to the Google Maps API
in order to retrieve the coordinates and addresses of the location sought. """

    def run_api(self, req):
        """ The module return the result of the Google Maps API. """
        api_key = GOOGLE_KEY
        print(api_key)
        gmaps_client = googlemaps.Client(api_key)
        geocode_result = gmaps_client.geocode(req, region='fr', language='fr')
        return geocode_result

    def run(self, req):
        """ This module filters the data and returns
        the address and geographic coordinates. """
        data = self.run_api(req)
        time.sleep(2)
        result = data[0]
        return result[
                   'formatted_address'], result[
                   'geometry']['location']['lat'], result[
                   'geometry']['location']['lng']

