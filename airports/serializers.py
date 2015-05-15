from rest_framework import serializers
from rest_framework import pagination

from .models import Airport

class AirportSerializer(serializers.ModelSerializer):
    read_only_fields = ('id','name','city','country','country_code','iata','icao')
    
    class Meta:
        model = Airport
        
class PaginationAirportSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = AirportSerializer