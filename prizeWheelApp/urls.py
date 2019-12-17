from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('index/', views.index, name='index'),
    path('noprize/', views.noPrize, name='noPrize'),
    path('prize/', views.prize, name='prize'),
    path('turntable/', views.turnTable, name='turnTable'),
    path('participated/', views.participated, name='participated'),

]
