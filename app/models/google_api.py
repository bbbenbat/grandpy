import googlemaps
import time


class GoogleApi:
    """  """

    def run(self, req):
        """  """
        api_key = 'AIzaSyByb99q8Q6CPiWRlkKLnWD4SxwlBZ8o4co'
        gmaps_client = googlemaps.Client(api_key)
        geocode_result = gmaps_client.geocode(req, region='fr', language='fr')
        time.sleep(2)
        result = geocode_result[0]
        return result['formatted_address'], \
               result['geometry']['location']['lat'], \
               result['geometry']['location']['lng']
