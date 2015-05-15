import json
import urllib2

from ..models import Airport
from .. import BasicAPI

ENDPOINT_URL = 'https://api.flightstats.com/flex/airports/rest/v1/json/'

class Flightstats(BasicAPI):
    
    is_multilingual = True
    
    def __init__(self,*args,**kwargs):
        self.app_id = kwargs['app_id']
        self.app_key = kwargs['app_key']
    
    def download(self,language=('en','English')):
        url = '%sactive?appId=%s&appKey=%s&extendedOptions=+languageCode:%s' % (ENDPOINT_URL, self.app_id, 
                                                                               self.app_key, language[0])
        print 'Fetching %s Airports from Flighstats.com' % language[1]
        data = json.load(urllib2.urlopen(url))
        return data
    
    def import_data(self, data, languages=None):
        print 'Starting import'
        if languages is None:
            loop_data = data
        else:
            loop_data = data[languages[0][0]]
        for i,tmp in enumerate(loop_data['airports']):
            
            try:
                t = Airport.objects.get(iata=tmp.get('iata',None),icao= tmp.get('icao',None))
            except Airport.DoesNotExist:
                t = Airport(iata=tmp.get('iata',None),icao= tmp.get('icao',None))
            
            if languages is not None:
                for lang_code, lang in languages:
                    setattr(t, 'city_%s' % lang_code, data[lang_code]['airports'][i]['city'])
                    setattr(t, 'country_%s' % lang_code, data[lang_code]['airports'][i]['countryName'])
                    setattr(t, 'name_%s' % lang_code, data[lang_code]['airports'][i]['name'])
            else:
                setattr(t, 'city', tmp['city'])
                setattr(t, 'country', tmp['countryName'])
                setattr(t, 'name', tmp['name'])
            setattr(t, 'country_code', tmp['countryCode'])
            setattr(t, 'time_zone', tmp.get('timeZoneRegionName',None))
            setattr(t, 'longitude', tmp.get('longitude',None))
            setattr(t, 'latitude', tmp.get('latitude',None))
            
            t.save()

