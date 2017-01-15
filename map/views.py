from .models import Place
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

def place_list(request):
    return Place.objects.all()

def near_place_list(request):
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))
    point = Point(lng, lat)
    return Place.objects.filter(point__distance_lt=(point, Distance(km=1)))
