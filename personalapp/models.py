from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit,ResizeToFill
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('personal', filename)

class Personal(models.Model):
    name = models.CharField(max_length=20)
    about_image = models.BooleanField(default=False)
    landing_image = models.BooleanField(default=False)
    image = models.ImageField(upload_to=get_file_path)

    about_img = ImageSpecField(source='image',
                                processors=[ResizeToFill(1280, 990)],
                                format='JPEG',
                                options={'quality': 100})

    def __str__(self):
        return self.name