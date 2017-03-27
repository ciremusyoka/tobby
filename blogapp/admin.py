from django.contrib import admin
from .models import Blog

class AdminBlog(admin.ModelAdmin):
    list_display = ['id','category','title','top_description','image_one','image_two','image_three','bottom_description']

admin.site.register(Blog,AdminBlog)
