# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_grado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('entidad', models.CharField(max_length=100)),
                ('año', models.CharField(max_length=4)),
            ],
            options={
                'ordering': ['año', 'nombre'],
            },
        ),
        migrations.AlterField(
            model_name='grado',
            name='año_egreso',
            field=models.CharField(max_length=4),
        ),
    ]
