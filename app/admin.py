from django.contrib import admin
from .models import *
class locationadmin(admin.ModelAdmin):
    list_display = ["id","latitude","longitude","timestamp"]



admin.site.register(Location,locationadmin)