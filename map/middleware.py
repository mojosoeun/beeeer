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
    json_list = []
    for instance in qs:
        json_list.append({
            'id': instance.id,
            'name': instance.name,
            'address' : instance.address,
            'lat': instance.lat,
            'lgn': instance.lng,
            'rating': instance.rating,
            'description': instance.description,
            'createdtime': instance.createdtime,
            'updatedtime': instance.updatedtime
            })
    return JsonResponse(json_list, safe=False)


class JsonResponseMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        if os.getenv('DISABLE_MIDDLEWARE'):
            raise MiddlewareNotUsed('DISABLE_MIDDLEWARE is set')

        super(JsonResponseMiddleware, self).__init__(*args, **kwargs)

    def process_request(self, request):
        if request.path == '/':
            return redirect('/all')

    def process_response(self, request, response):
        if isinstance(response, QuerySet):
            return json_response(response)
        return response
