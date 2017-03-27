from django.contrib import admin
from .models import Message

class AdminMessage(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'message', 'date']

admin.site.register(Message,AdminMessage)
