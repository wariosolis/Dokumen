# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20171219_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='folder',
            field=models.ManyToManyField(help_text='select the folders you want to exclude', related_name='role', to='common.Carpeta', verbose_name='Folder'),
        ),
    ]
