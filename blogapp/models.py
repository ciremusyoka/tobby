from __future__ import unicode_literals

from django.db import models
from imagesapp.models import Image

class Blog(models.Model):
    type=(('W','weddings'),('PW','pre-weddings'))
    category =models.CharField(max_length=20, choices=(type))
    title = models.CharField(max_length=50)
    top_description = models.TextField()
    image_one = models.ForeignKey(Image, related_name='image_one')
    image_two = models.ForeignKey(Image, related_name='image_two')
    image_three = models.ForeignKey(Image, related_name='image_three')
    bottom_description = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.title
