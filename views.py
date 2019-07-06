# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    ayoub = "ayoub"
    my_dict = {'insert_me':ayoub}
    return render(request,'index.html',context=my_dict)
def help(request):
    problem = "SQL injection "
    dict = {'here':problem}
    return render(request,'help.html',context=dict)

# Create your views here.
