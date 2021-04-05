from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'baza'
urlpatterns = [
    path('', views.home, name='home'),
    path('highest-prices/', views.highest, name='highest'),
    path('lowest-prices/', views.lowest, name='lowest-prices'),
    path('avg/', views.avg, name='avg'),
    path('modelsByBrand/', views.modelsByBrand, name='modelsByBrand'),
    path('avgPrice/', views.avaragePrices, name='avaragePrices'),
    path('chart/', views.chart, name='chart'),
    path('searchBrand/', views.searchBrand, name='searchBrand'),
    path('allModels/', views.allModels, name='allModels'),
    path('searchModel/', views.searchModel, name='searchModel'),
    path('searchPrice/', views.searchPrice, name='searchPrice'),
    path('filterPrice/', views.filterPrice, name='filterPrice'),
    path('chartPrice/', views.chartPrice, name='chartPrice')
]