from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

def main(request):
    return render(request, 'index_main.html', {'index': models.Index.objects.all().latest('pk')})

def index(request):
    return render(request, 'index.html', {'index': models.Index.objects.all().latest('pk'), 'contact': models.Contact.objects.all().latest('pk'), 'clients': models.Client.objects.all(), 'testimonials1': models.Testimonial.objects.filter(id='1'),'testimonials': models.Testimonial.objects.all(), 'team': models.Team.objects.all(), 'services': models.Service.objects.all()})

def clients(request):
    return render(request, 'clients.html', {'index': models.Index.objects.all().latest('pk'), 'clients': models.Client.objects.all(), 'contact': models.Contact.objects.all().latest('pk')})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        response_email = render_to_string('response_email.html', {'name': name})
        mail = EmailMultiAlternatives('Thanks for response', response_email, settings.EMAIL_HOST_USER, [email])
        mail.content_subtype = 'html'
        mail.send()

        send_mail('Message from WordDealers Contact Form | Subject: '+subject, 'Name: '+name+'\n'+'Email: '+email+'\n'+'Subject: '+subject+'\n'+'Message: '+message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])        
        return HttpResponseRedirect('contact')
    else:    
        return render(request, 'contact.html', {'index': models.Index.objects.all().latest('pk'), 'contact': models.Contact.objects.all().latest('pk')})