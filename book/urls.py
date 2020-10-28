from django.contrib import admin
from django.urls import path
from .views import sendmail

urlpatterns = [
    path('sendmail/', sendmail),
]
