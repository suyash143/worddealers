from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Index)
admin.site.register(models.Client)
admin.site.register(models.Testimonial)
admin.site.register(models.Team)