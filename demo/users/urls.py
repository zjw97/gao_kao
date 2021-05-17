# -*- coding: UTF-8 -*-
from django.urls import path, re_path

from users import views

urlpatterns = [
    path('index/', views.hello),  # 首页
    path('login/', views.login),  # 登录
    re_path(r'^say/', views.say),  # 路由解析的执行顺序由上至下，且会有屏蔽效应
    re_path(r'^sayweizi/', views.say),
]