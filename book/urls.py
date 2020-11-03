from django.contrib import admin
from django.urls import path
from .views import detailview, redirectedview

urlpatterns = [
    path('detail/<int:pk>', detailview),
    path('redirected/<int:pk>', redirectedview)
]
