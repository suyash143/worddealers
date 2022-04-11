from django.shortcuts import render
from . import models

def main(request):
    return render(request, 'index_main.html', {'index': models.Index.objects.all().latest('pk')})

def index(request):
    return render(request, 'index.html', {'index': models.Index.objects.all().latest('pk'), 'clients': models.Client.objects.all()})

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

