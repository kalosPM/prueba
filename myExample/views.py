#encoding:utf-8
from __future__ import unicode_literals

from django.shortcuts import render,  redirect

# Create your views here.
def login(request):
    return render(request, 'index.html', locals())