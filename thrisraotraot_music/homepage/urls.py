# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:37:48 2023

@author: user
"""

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]

app_name = "homepage"