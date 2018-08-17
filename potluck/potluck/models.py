# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    DISH_TYPE_CHOICES = (
                        ('Appetizer', 'Appetizer'),
                        ('Main_course', 'Main course'),
                        ('Dessert', 'Dessert'),
    )
    dish_type = models.CharField(max_length=20,
                                 verbose_name='Dish type',
                                 choices=DISH_TYPE_CHOICES,
                                 default='Main_Course')
    dish = models.CharField(max_length=200,
                            verbose_name='Dish Name',
                            default=' ')
    common_allergy_ingredients = models.CharField(max_length=200,
                                                  verbose_name='What is in your dish that others might be allergic to?',
                                                  blank=True,
                                                  null=True)
    crockpot = models.BooleanField(verbose_name='will this dish come in a container that will need an outlet?',
                                   default=False)

    def __str__(self):
        return self.name
