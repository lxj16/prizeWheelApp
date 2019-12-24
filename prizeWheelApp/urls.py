from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('ctrl', views.start, name='start'),
    path('', views.Index.as_view(), name='index'),
    path('noprize/', views.noPrize, name='noPrize'),
    path('prize/<int:prizeID>', views.PrizeView.as_view(), name='prize'),
    path('turntable/check/<int:prizeID>', views.check_prize, name='check_prize'),
    path('turntable/<int:phoneNumber>',
         views.TurnTable.as_view(), name='turnTable'),
    path('participated/', views.participated, name='participated'),

]
