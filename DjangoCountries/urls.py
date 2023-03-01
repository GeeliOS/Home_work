from django.urls import path
from MainApp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('languages-list', views.languages_list, name='languages-list'),
    path('countries-list', views.countries_list, name='countries-list'),
    path('countrie/<str:name>', views.countrie, name='countrie'),
    path('language_countrys/<str:name>', views.language_countrys, name='language_countrys'),
]


