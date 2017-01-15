from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    address = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()
    rating = models.FloatField(default=0.00)
    description = models.TextField(blank=True, null=True)
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    point = models.PointField(blank=True, null=True)
    objects = models.GeoManager()


    def save(self, *args, **kwargs):
        self.point = Point(self.lon, self.lat)
        super().save(*args, **kwargs)

    # Returns the string representation of the model.
    def __str__(self):  # __unicode__ on Python 2
        return self.name
