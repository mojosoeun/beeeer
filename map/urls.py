from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all/$', views.place_list),
    url(r'^near/$', views.near_place_list),

]
