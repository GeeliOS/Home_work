from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # TODO: вы добавили имена url'ам, но этими именами в шаблонах не пользуетесь
    # TODO: главная страница отсутствует
    path('about', views.about, name='about'),
    path('languages-list', views.languages_list, name='languages-list'),
    path('countries-list', views.countries_list, name='countries-list'),
    path('countrie/<str:name>', views.countrie, name='countrie'),
]


