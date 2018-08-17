# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Items
from .forms import ItemsForm


def index(request):
    if request.method == 'POST':

        if 'volunteer' in request.POST:
            form = ItemsForm()
            context = {
                'form': form,
            }
            return render(request, 'form.html', context)
        # if 'submit_dish' in request.POST:
        else:
            form = ItemsForm(request.POST)
            if form.is_valid():
                form.save()
                items_list = Items.objects.order_by('name')
                context = {
                    'items_list': items_list,
                }
                return render(request, 'list.html', context)
            else:
                form = ItemsForm()
                context = {
                    'form': form,
                }
                return render(request, 'list.html', context)
    else:
        items_list = Items.objects.order_by('name')
        context = {
            'items_list': items_list,
        }
        return render(request, 'list.html', context)
    # return HttpResponse(template.render(context, request))
