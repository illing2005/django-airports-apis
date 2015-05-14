from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ...models import Airport
from ... import get_airport_api

from optparse import make_option

class Command(BaseCommand):
    help = """Imports airport data from in settings specified api"""
    option_list = BaseCommand.option_list + (
        make_option('--flush', action='store_true', default=False,
            help="Delete all airport data."
        ),
    )    
    
    def handle(self,*args,**options):
        
        if options['flush'] == True:
            Airport.objects.all().delete()
        else:
            airport_api = get_airport_api()
            fn = airport_api.download()
            airport_api.import_data(fn)
        