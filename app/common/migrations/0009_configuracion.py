# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20171121_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modify')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('url_biblioteca', models.URLField(verbose_name='Biblioteca')),
                ('url_academico', models.URLField(verbose_name='Academico')),
                ('url_convocatoria', models.URLField(verbose_name='Convocatorias')),
                ('archivo', models.ImageField(upload_to='configuracion/%Y/%m/%d/', verbose_name='Logo')),
            ],
            options={
                'db_table': 'configuracion',
                'verbose_name': 'Configuracion',
                'verbose_name_plural': 'Configuracion',
                'default_related_name': 'configuracion',
            },
        ),
    ]