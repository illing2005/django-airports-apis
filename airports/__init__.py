import abc
from django.conf import settings

AIRPORT_API = {'openflights': ('airports.openflights.OpenFlights',{})}

def get_airport_api():
    airport_api =  getattr(settings, 'AIRPORT_API', AIRPORT_API)
    key = airport_api.keys()[0]
    handler,config = airport_api.get(key,(None,None))
    path = handler.split('.')
    module_path = str('.'.join(path[:-1]))
    class_name = str(path[-1])
    module = __import__(module_path, globals(), locals(), [class_name])
    class_ = getattr(module, class_name)
    return class_(**config)


class BasicAPI(object):
    '''
    This class defines the basic API. 
    '''
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def download(self):
        pass
    
    @abc.abstractmethod    
    def import_data(self, data):
        pass