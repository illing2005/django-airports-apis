from django.contrib import admin
from .models import Airport

class AirportAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "iata", "icao", "city", "country")
    search_fields = ("name", "iata", "icao")

admin.site.register(Airport, AirportAdmin)
