# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potluck', '0002_auto_20171107_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='dish_type',
            field=models.CharField(choices=[('Appetizer', 'Appetizer'), ('Main_course', 'Main course'), ('Dessert', 'Dessert')], default='Main_Course', max_length=20, verbose_name='Dish type'),
        ),
    ]