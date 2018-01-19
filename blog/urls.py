# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:45:51 2017

@author: alexkreamas
"""

from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^$', views.post_list, name = 'post_list'),
               url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
               url(r'^post/new/$', views.post_new, name = 'post_new'),
               url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name = 'post_edit'),

               url(r'^post/mensaje1/$', views.post_msj1, name = 'post_msj1'),
               url(r'^post/mensaje2/$', views.post_msj2, name = 'post_msj2'),

               url(r'search$', views.search, name='search'),

               url(r'subefile$', views.subefile, name='subefile'),

]