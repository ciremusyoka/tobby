from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    message =models.TextField()
    date = models.DateTimeField(auto_now=True)
