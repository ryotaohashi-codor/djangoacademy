from django.contrib import admin
from django.urls import path
from .views import indexview

urlpatterns = [
    path('page/', indexview),
]
