from django.db import models
from PIL import Image


# Create your models here.


class Stat(models.Model):
    stat_text = models.CharField(max_length=20, blank=False)
    stat_number = models.CharField(max_length=20, blank=False)
    stat_icon = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return str(self.stat_text)


class Index(models.Model):
    tagline = models.TextField(max_length=100)
    main_heading = models.TextField(max_length=100, null=True)
    about = models.TextField(max_length=500, null=True)
    stats = models.ManyToManyField(Stat, blank=True)
    team_heading = models.TextField(max_length=200, null=True)
    services_heading = models.TextField(max_length=200, null=True)
    portfolio = models.TextField(max_length=200, null=True)
    contact_description = models.TextField(max_length=200, null=True)
    # address = models.CharField(max_length=150, null= True)
    # number = models.CharField(max_length=150, null= True)
    facebook_link = models.URLField(max_length=150, null=True, blank=True)
    twitter_link = models.URLField(max_length=150, null=True, blank=True)
    linkedin_link = models.URLField(max_length=150, null=True, blank=True)
    instagram_link = models.URLField(max_length=150, null=True, blank=True)


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


class Achievements(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    image = models.ImageField(upload_to='achievements', null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Team(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team', null=True, blank=True, default='images/team/worddealers.png')
    facebook_link = models.URLField(max_length=100, null=True, blank=True)
    twitter_link = models.URLField(max_length=100, null=True, blank=True)
    linkedin_link = models.URLField(max_length=100, null=True, blank=True)
    instagram_link = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self):
        super().save()
        print("Yeah")
        divisor = 1
        alignx = 0.5
        aligny = 0.5
        aspect = 1
        img = Image.open(self.image.path)

        if img.width / img.height > aspect / divisor:
            newwidth = int(img.height * (aspect / divisor))
            newheight = img.height
        else:
            newwidth = img.width
            newheight = int(img.width / (aspect / divisor))
        imgp = img.crop((alignx * (img.width - newwidth),
                         aligny * (img.height - newheight),
                         alignx * (img.width - newwidth) + newwidth,
                         aligny * (img.height - newheight) + newheight))

        imgp.save(self.image.path)


class Service(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False)
    icon = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    contact_page_heading = models.CharField(max_length=50, blank=False)
    contact_page_para = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=150, null=True)
    map_link = models.URLField(null=True)
    email = models.CharField(max_length=150, null=True)
    number = models.CharField(max_length=150, null=True)
    work_time = models.CharField(max_length=150, null=True)


class Award(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    image = models.ImageField(upload_to='awards', null=True, blank=True)

    def __str__(self):
        return str(self.title)