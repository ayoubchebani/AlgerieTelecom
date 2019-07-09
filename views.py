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

def button1(request):
    return render(request,'index.html')

def funct1(request):
    print("unconfined")
    data = "ayoub"
    clicked = True
    
    return render(request,'index.html',context={'data':data})

def button2(request):
    data = "ayoub"
    return render(request,'index.html',context={'data':data})

def funct2(request):
    mandatory = "mandatory"
    print("ayoub mandatory")
    dictionnary = {'data':mandatory}
    
    return render(request,'index.html',context=dictionnary)

def menu(request):
    return render(request, 'menu.html')


