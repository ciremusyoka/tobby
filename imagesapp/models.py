from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit,ResizeToFill
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media', filename)

class Image(models.Model):
    types = (('W','wedding'),('PO','portrait'),('PE','personal'),('LS','landscape'))
    category = models.CharField(max_length=15, choices=(types))
    name = models.CharField(max_length=20)
    public = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    image = models.ImageField(upload_to=get_file_path)
    dominantColor = models.CharField(max_length=20,null=True,blank=True)

    preview_xs = ImageSpecField(source='image',
                                processors=[ResizeToFit(height=768)],
                                format='JPEG',
                                options={'quality': 60})
    preview_xxs = ImageSpecField(source='image',
                                      processors=[ResizeToFit(height=375)],
                                      format='JPEG',
                                      options={'quality': 60})

    preview_s = ImageSpecField(source='image',
                                      processors=[ResizeToFit(height=1080)],
                                      format='JPEG',
                                      options={'quality': 60})
    preview_m = ImageSpecField(source='image',
                                      processors=[ResizeToFit(height=1600)],
                                      format='JPEG',
                                      options={'quality': 70})
    preview_l = ImageSpecField(source='image',
                                      processors=[ResizeToFit(height=2160)],
                                      format='JPEG',
                                      options={'quality': 80})
    preview_xl = ImageSpecField(source='image',
                                processors=[ResizeToFit(height=2880)],
                                format='JPEG',
                                options={'quality': 90})
    card_image = ImageSpecField(source='image',
                                processors=[ResizeToFill(265, 180)],
                                format='JPEG',
                                options={'quality': 100})
    details_image = ImageSpecField(source='image',
                                processors=[ResizeToFill(800, 537)],
                                format='JPEG',
                                options={'quality': 100})


    def __str__(self):
        return self.name







