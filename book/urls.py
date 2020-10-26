from django.contrib import admin
from django.urls import path
from .views import downloadview

urlpatterns = [
    path('download/<int:pk>', downloadview),
]
