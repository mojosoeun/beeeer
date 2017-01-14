import os
from django.http import JsonResponse
from django.db.models.query import QuerySet

from django.core.exceptions import MiddlewareNotUsed
from django.shortcuts import redirect

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

def json_response(qs):
    mylist = []
    for instance in qs:
        mylist.append({
            'id': instance.id,
            'name': instance.name,
            'korean_address' : instance.korean_address,
            'english_address' : instance.english_address,
            'lon': instance.lon,
            'lat': instance.lat,
            'rating': instance.rating,
            'desc': instance.desc,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at
        })
    return JsonResponse(mylist, safe=False)


class JsonResponseMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        if os.getenv('DISABLE_MIDDLEWARE'):
            raise MiddlewareNotUsed('DISABLE_MIDDLEWARE is set')

        super(JsonResponseMiddleware, self).__init__(*args, **kwargs)

    def process_request(self, request):
        if request.path == '/':
            return redirect('/post')

    def process_response(self, request, response):
        if isinstance(response, QuerySet):
            return json_response(response)
        return response
