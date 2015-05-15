import json
import urllib2

from ..models import Airport
from .. import BasicAPI

ENDPOINT_URL = 'https://api.flightstats.com/flex/airports/rest/v1/json/'

class Flightstats(BasicAPI):
    
    def __init__(self,*args,**kwargs):
        self.app_id = kwargs['app_id']
        self.app_key = kwargs['app_key']
    
    def download(self,language='de'):
        url = '%sactive?appId=%s&appKey=%s&extendedOptions=+languageCode:%s' % (ENDPOINT_URL, self.app_id, 
                                                                               self.app_key, language)
        print 'Fetching Airports from Flighstats.com'
        data = json.load(urllib2.urlopen(url))
        return data
    
    def import_data(self, data):
        print 'Starting import'
        for i,tmp in enumerate(data['airports']):
            iata = tmp.get('iata',None)
            icao = tmp.get('icao',None)
            city = tmp['city']
            country = tmp['countryName']
            name = tmp['name']
            country_code = tmp['countryCode']
            time_zone = tmp.get('timeZoneRegionName',None)
            longitude = tmp.get('longitude',None)
            latitude = tmp.get('latitude',None)
             
            Airport.objects.get_or_create(city=city,country=country,name=name,
#                                                   city=city,country=country,name=name,
                                country_code=country_code,iata=iata,icao=icao,
                                time_zone=time_zone, longitude=longitude, latitude=latitude)
