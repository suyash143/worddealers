from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Index)
admin.site.register(models.Client)
admin.site.register(models.Testimonial)
admin.site.register(models.Team)
admin.site.register(models.Service)
admin.site.register(models.Stat)

admin.site.site_header = 'WordDealers Admin Panel'
admin.site.site_title = 'WordDealers Admin Panel'