from django.shortcuts import render
from .models import Book
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

def detailview(request, pk):
    object = Book.objects.get(pk=pk)
    return redirect(object)


def redirectedview(request, pk):
    object = Book.objects.get(pk=pk)
    return HttpResponse('redirected')