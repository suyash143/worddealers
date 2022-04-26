from django.shortcuts import render
from . import models

def main(request):
    return render(request, 'index_main.html', {'index': models.Index.objects.all().latest('pk')})

def index(request):
    return render(request, 'index.html', {'index': models.Index.objects.all().latest('pk'), 'clients': models.Client.objects.all(), 'testimonial': models.Testimonial.objects.all(), 'team': models.Team.objects.all(), 'services': models.Service.objects.all()})

