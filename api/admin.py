from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin, ModelAdmin
from .models import *
admin.site.register(Categories)
admin.site.register(SubCategory)
admin.site.register(Products)
