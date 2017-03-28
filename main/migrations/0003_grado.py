# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comunidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10)),
                ('año_egreso', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['año_egreso'],
            },
        ),
    ]