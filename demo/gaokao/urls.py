from django.urls import path, re_path
from gaokao import views
from django.contrib import admin

urlpatterns = [
    path('search_school/', views.search_school),
    path('admin/', admin.site.urls),
]
