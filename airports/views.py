from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Airport
from .serializers import PaginationAirportSerializer
from django.views.decorators.cache import cache_page

@api_view(['GET'])
@cache_page(60 * 15)
def airport_list(request): 
    q = request.GET.get('q',None)
    page = request.GET.get('page',1)
    items_per_page = request.GET.get('items_per_page',30)
    if q:
        obs = Airport.objects.filter(Q(name__icontains=q) | Q(city__icontains=q) | Q(iata__icontains=q)).exclude(iata__isnull=True).order_by('country') 
    else:
        obs = Airport.objects.all().exclude(iata__isnull=True).order_by('country')
    
    #Paginate:
    paginator = Paginator(obs,items_per_page)
    try:
        airports = paginator.page(page)
    except PageNotAnInteger:
        airports = paginator.page(1)
    except EmptyPage:
        airports = paginator.page(paginator.num_pages)
    
    #serializer = AirportSerializer(airports,many=True)
    serializer = PaginationAirportSerializer(airports)
    return Response(serializer.data)