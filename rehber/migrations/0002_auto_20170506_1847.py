# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisitelefon',
            name='KisiTelefonID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kisitelefon',
            name='Telefon',
            field=models.CharField(max_length=13, verbose_name='Telefon'),
        ),
    ]
