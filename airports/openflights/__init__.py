import requests
import os
import csv
from ..models import Airport
from .. import BasicAPI

ENDPOINT_URL = "https://sourceforge.net/p/openflights/code/HEAD/tree/openflights/data/airports.dat?format=raw"
APP_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))

class OpenFlights(BasicAPI):
    
    data_dir = os.path.join(APP_DIR, 'data')
    
    def download(self, filename='tmp.dat'):  
        print 'Fetching Airports from openflights'
        response = requests.post(ENDPOINT_URL, data={})
        filepath = os.path.join(self.data_dir, filename)
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        fobj = open(filepath, 'w')
        fobj.write(response.text.encode('utf-8'))
        fobj.close()
        return filepath
    
    def import_data(self, fn):
        print 'Starting import'
        with open(fn) as f:
            reader = csv.reader(f)
            for row in reader:
                Airport.objects.get_or_create(name=row[1],
                                              city=row[2],
                                              country=row[3],
                                              iata=row[4],
                                              icao=row[5],
                                              latitude=row[6],
                                              longitude=row[7],
                                              time_zone=row[9])
        
        
    