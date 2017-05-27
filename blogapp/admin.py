from django.contrib import admin
from .models import Blog

class AdminBlog(admin.ModelAdmin):
    list_display = ['id','category','title','description','image', 'preview']

admin.site.register(Blog,AdminBlog)
