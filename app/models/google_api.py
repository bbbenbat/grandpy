import time
import os

import googlemaps

GOOGLE_KEY = os.getenv('GOOGLE_API_KEY')


class GoogleApi:
    """  """

    def run_api(self, req):
        """  """
        api_key = GOOGLE_KEY
        gmaps_client = googlemaps.Client(api_key)
        geocode_result = gmaps_client.geocode(req, region='fr', language='fr')
        return geocode_result

    def run(self, req):
        """  """
        data = self.run_api(req)
        time.sleep(2)
        result = data[0]
        return result['formatted_address'], result['geometry']['location']['lat'], result['geometry']['location']['lng']


