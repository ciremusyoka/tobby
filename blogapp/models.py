from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagesapp.models import Image
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class Blog(models.Model):
    type=(('weddings','weddings'),('pre-weddings','pre-weddings'),('family','family'),('portrait','portrait'),('personal','personal'),('landscape','landscape'))
    category = models.CharField(max_length=20, choices=(type))
    title = models.CharField(max_length=50)
    preview = models.CharField(max_length=200)
    description = RichTextUploadingField()
    image = models.ForeignKey(Image, related_name='image_one', )

    def __str__(self):
        return self.title
