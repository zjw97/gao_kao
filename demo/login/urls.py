from django.urls import path
from login import views

urlpatterns = [
    path(r'', views.index),
    path('login/', views.log_in, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.log_out, name="logout")
]