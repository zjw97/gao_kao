# -*- coding: UTF-8 -*-
from django.urls import re_path
from weather import views

urlpatterns = [
    re_path(r'hangzhou/', views.weather)
]