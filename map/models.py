from __future__ import unicode_literals
from django.contrib.gis.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()
    rating = models.FloatField(default=0.00)
    description = models.TextField(blank=True, null=True)

    # Returns the string representation of the model.
    def __str__(self):  # __unicode__ on Python 2
        return self.name
