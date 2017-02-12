import os
from django.http import JsonResponse
from django.db.models.query import QuerySet

from django.core.exceptions import MiddlewareNotUsed
from django.shortcuts import redirect
from django.core.files.storage import default_storage as storage


try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

def get_image_url(image):
    if not image:
        return ""
    file_path = image.name
    if storage.exists(file_path):
        return storage.url(file_path)
    return ""

def json_response(qs):
    json_list = []
    for instance in qs:
        json_list.append({
            'id': instance.id,
            'name': instance.name,
            'image' : get_image_url(instance.image),
            'address' : instance.address,
            'lat': instance.lat,
            'lon': instance.lon,
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

    def process_response(self, request, response):
        if isinstance(response, QuerySet):
            return json_response(response)
        return response
