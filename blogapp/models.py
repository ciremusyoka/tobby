from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagesapp.models import Image
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class Blog(models.Model):
    type=(('weddings','weddings'),('pre-weddings','pre-weddings'),('family','family'),('portrait','portrait'),('personal','personal'),('landscape','landscape'))
    category =models.CharField(max_length=20, choices=(type))
    title = models.CharField(max_length=50)
    top_description = RichTextUploadingField()
    image_one = models.ForeignKey(Image, related_name='image_one',)
    image_two = models.ForeignKey(Image, related_name='image_two', null=True, blank=True)
    image_three = models.ForeignKey(Image, related_name='image_three', null=True, blank=True)
    bottom_description = RichTextUploadingField( null=True, blank=True)


    def __str__(self):
        return self.title
