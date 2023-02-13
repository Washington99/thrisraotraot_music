# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:57:19 2023

@author: user
"""

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]

# This might be needed, depending on your Django version
app_name = "contact"