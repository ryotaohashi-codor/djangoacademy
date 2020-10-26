from django.shortcuts import render, get_object_or_404
from .models import FileUpload
from django.http import HttpResponse
import mimetypes
import shutil

# Create your views here.

def downloadview(request, pk):
    object = get_object_or_404(FileUpload, pk=pk)
    file = object.files
    name = file.name
    response = HttpResponse(content_type=mimetypes.guess_type(name)[0] or 'application/octet-stream')
    response['Content-Disposition'] = f'attachement; filename={name}'
    shutil.copyfileobj(file, response)
    return response