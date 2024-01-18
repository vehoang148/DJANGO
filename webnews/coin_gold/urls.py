
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='coin-list'),
     path('/gold', views.gold_list, name='gold-list')
]
