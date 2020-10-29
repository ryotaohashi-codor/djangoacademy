from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flatpage/',include('django.contrib.flatpages.urls')),
    path('',include('book.urls')),
]
