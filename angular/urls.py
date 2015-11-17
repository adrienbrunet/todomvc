# coding: utf-8

# Adrien Brunet <brunet.adrien@gmail.com>


from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^', views.todo_angular, name='todo_angular'),
]
