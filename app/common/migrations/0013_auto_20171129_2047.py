# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-29 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_auto_20171129_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='archivo_ayuda',
            field=models.FileField(blank=True, null=True, upload_to='configuracion/%Y/%m/%d/', verbose_name='Archivo de ayuda'),
        ),
    ]
