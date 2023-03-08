from django.contrib import admin
from .models import *


'''
class BrandAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
    admin.site.register(Brand,BrandAdmin)
'''
admin.site.register(Brand)
admin.site.register(Product)
