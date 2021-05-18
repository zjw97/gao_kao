from django.urls import path
from gaokao import views

urlpatterns = [

    path('search_school/', views.search_school),
]
