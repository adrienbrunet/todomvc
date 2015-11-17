# coding: utf-8

# Adrien Brunet <brunet.adrien@gmail.com>


from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('angular.urls')),
]
