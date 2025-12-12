from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Data)

admin.site.register(SmallData)

admin.site.register(SmallestData)

# @admin.register(Data)
# class DataAdmin(admin.ModelAdmin):
#     list_display =('name','age')