# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesapp', '0002_auto_20170425_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='all',
            new_name='featured',
        ),
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('W', 'wedding'), ('F', 'family'), ('PO', 'portrait'), ('PE', 'personal'), ('LS', 'landscape')], max_length=15),
        ),
    ]