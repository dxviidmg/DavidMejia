# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-05-18 17:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190518_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comunidad',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Comunidades'},
        ),
        migrations.AlterModelOptions(
            name='interes',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Intereses'},
        ),
        migrations.AlterModelOptions(
            name='publicacion',
            options={'ordering': ['año', 'titulo'], 'verbose_name_plural': 'Publicaciones'},
        ),
    ]
