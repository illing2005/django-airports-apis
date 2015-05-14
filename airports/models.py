# -*- coding: utf-8 -*-
from django.db import models

class Airport(models.Model):
    
    iata = models.CharField(max_length=3, null = True, blank=True)
    icao = models.CharField(max_length=4, null = True, blank=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10, null=True, blank=True)
    time_zone = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return '%s %s' % (self.iata,self.name)
