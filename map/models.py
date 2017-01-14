from __future__ import unicode_literals
from django.contrib.gis.db import models

class Bar(models.Model):
    name = models.CharField(max_length=50)
    korean_address = models.CharField(max_length=100)
    english_address = models.CharField(max_length=100)
    lon = models.FloatField()
    lat = models.FloatField()
    rating = models.FloatField(default=0.00)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Returns the string representation of the model.
    def __str__(self):  # __unicode__ on Python 2
        return self.name
