
from django.conf import settings

AIRPORT_API = {'openflights': ('airports.openflights.OpenFlights',{})}

AIRPORT_API = {'flighstats': ('airports.flightstats.Flightstats',
                              {'app_id' : 'da983eec',
                               'app_key' : 'fbaaefd87bba19e7990259d7440a7ee6'}),}

def get_airport_api():
    
    airport_api =  getattr(settings, 'AIRPORT_API', AIRPORT_API)
    key = airport_api.keys()[0]
    handler,config = airport_api.get(key,(None,None))
    print handler,config
    path = handler.split('.')
    module_path = str('.'.join(path[:-1]))
    class_name = str(path[-1])
    module = __import__(module_path, globals(), locals(), [class_name])
    class_ = getattr(module, class_name)
    return class_(**config)