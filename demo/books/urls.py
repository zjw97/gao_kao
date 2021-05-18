from django.urls import path
from books import views

urlpatterns = [
    #path('add_book/', views.add_book),
    #path('all_book/', views.all_book),
    #path('filter_book/', views.filter_book),
    #path('exclude_book/', views.exclude_book),
    #path('order_book/', views.order_book),
    #path('count_book/', views.count_book),
    #path('first_book/', views.first_book),
    #path('last_book/', views.last_book),
    #path('exist_book/', views.exist_book),
    #path('value_book/', views.value_book),
    path('search_book/', views.search_book),
]
