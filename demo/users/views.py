from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    """第一个视图 hello"""
    return HttpResponse("Hello World!" )

def login(request):
    return HttpResponse("用户登录界面")

def say(request):
    return HttpResponse("say")

def sayweizi(request):
    return HttpResponse("sayweizi!")