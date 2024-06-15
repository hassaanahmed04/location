from django.db import models

class Location(models.Model):
    
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


