from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('languages-list', views.languages_list),
    path('countries-list', views.countries_list),
    path('countrie/<str:name>', views.countrie),
]


