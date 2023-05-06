from django.contrib import admin
from django.urls import path, include
from .views import formview, displayview, filterdisplay

urlpatterns = [
    path('input/', formview),
    path('display/', displayview),
    path('filterdisplay/', filterdisplay),
]
