from django.contrib import admin
from django.urls import path
from .views import detailview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:pk>/', detailview),
]
