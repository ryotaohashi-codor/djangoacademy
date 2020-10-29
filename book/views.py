from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator

# Create your views here.

def indexview(request):
    object_list = Book.objects.all()
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page', 1)
    paginated_list = paginator.page(page)
    return render(request, 'index.html', {'paginated_list':paginated_list})