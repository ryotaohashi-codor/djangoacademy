from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Book

# Create your views here.

def detailview(request, pk):
    object = get_object_or_404(Book, pk=pk)
    return render(request, 'detail.html', {'object':object})