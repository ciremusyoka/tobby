from django.contrib import admin
from .models import Image

class adminimages(admin.ModelAdmin):
    list_display = ['id', 'category','featured','public','name', 'image', 'dominantColor']

admin.site.register(Image,adminimages)

