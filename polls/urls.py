# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:43:25 2017

@author: alexkreamas
"""

from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^$', views.index, name = 'index'),
]