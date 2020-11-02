from django.contrib import admin
from django.urls import path
from .views import requestfunction

urlpatterns = [
    path('request/', requestfunction)
]
