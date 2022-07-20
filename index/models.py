from asyncio.windows_events import NULL
from cgitb import enable
from turtle import heading
from os import link
from django.db import models

# Create your models here.

class Stat(models.Model):
    stat_text = models.CharField(max_length=20, blank=False)
    stat_number = models.CharField(max_length=20, blank=False)
    stat_icon = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return str(self.stat_text)

class Index(models.Model):
    tagline = models.TextField(max_length=100)
    main_heading = models.TextField(max_length=100, null= True)
    about = models.TextField(max_length=500, null= True)
    stats = models.ManyToManyField(Stat, null=True)
    team_heading = models.TextField(max_length=200, null= True)
    services_heading = models.TextField(max_length=200, null= True)
    portfolio = models.TextField(max_length=200, null= True)
    contact_description = models.TextField(max_length=200, null= True)
    # address = models.CharField(max_length=150, null= True)
    # number = models.CharField(max_length=150, null= True)
    facebook_link = models.URLField(max_length=150, null= True, blank=True)
    twitter_link = models.URLField(max_length=150, null= True, blank=True)
    linkedin_link = models.URLField(max_length=150, null= True, blank=True)
    instagram_link = models.URLField(max_length=150, null= True, blank=True)

class Client(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='clients', null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Testimonial(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='testimonial', null=True, blank=True)
    testimonial = models.TextField(max_length=100)

    def __str__(self):
        return str(self.name)

class Team(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team', null=True, blank=True)
    facebook_link = models.URLField(max_length=100, null=True, blank=True)
    twitter_link = models.URLField(max_length=100, null=True, blank=True)
    linkedin_link = models.URLField(max_length=100, null=True, blank=True)
    instagram_link = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Service(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False)
    icon = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    contact_page_heading = models.CharField(max_length=50, blank=False)
    contact_page_para = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=150, null= True)
    map_link = models.URLField(default=NULL)
    email = models.CharField(max_length=150, null= True)
    number = models.CharField(max_length=150, null= True)
    work_time = models.CharField(max_length=150, null= True)
