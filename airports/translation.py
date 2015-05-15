from modeltranslation.translator import translator, TranslationOptions
from airports.models import Airport

class AirportTranslationOptions(TranslationOptions):
    fields = ['name', 'city', 'country']
    
translator.register(Airport, AirportTranslationOptions)