from django.urls import path
from . import views




urlpatterns = [
    path('news/', views.news_list, name='list_news'),
    path('news/<int:pk>/', views.new_single, name='new_single'),
]