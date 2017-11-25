# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    num = random.randint(0, 1000)
    ls = [num, random.randint(0, 1000), random.randint(0, 1000)]
    context = {"var": True, "bool_item": True, "num": num, "list": ls}
    return render(request, "base.html", context)
