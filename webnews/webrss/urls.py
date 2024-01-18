from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('/news', views.index_new, name='news'),
    path('/wolrd', views.index_wolrd, name='wolrd'),
    path('/business', views.index_business, name='business'),
    path('/sport', views.index_sport, name='sport'),
    path('/entertainment', views.index_entertainment, name='entertainment'),
    path('/health', views.index_health, name='health'),
    path('/life', views.index_life, name='life'),
    path('/science', views.index_science, name='science'),
    path('/education', views.index_education, name='education'),



    path('/weather', views.weatherApi, name='weather_api'), 
    path('/coin', views.coin_list, name='coin-list'),
    path('/gold', views.gold_list, name='gold-list')
]
