from django.urls import path,include

from homepage import views



urlpatterns = [

    path('', views.str_home, name='home'),
    path('contact/',views.contact, name='inf'),
    path('home/',views.str_home, name='hm2'),

]
