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

#def button1(request):
#    return render(request,'index.html')

def funct1(request):
    print("unconfined")
    data = "ayoub"
    clicked = True
    
    return render(request,'index.html',context={'data':data})




def funct2(request):
    mandatory = "mandatory"
    print("ayoub mandatory")
    dictionnary = {'data':mandatory}
    
    return render(request,'index.html',context=dictionnary)

def Kids_profile(request):
    kids = 'kids'
    print(kids)
    return render(request,'menu.html',context={'data':kids})

def Gaming_profile(request):
    gaming = 'gaming'
    print(gaming)
    return render(request,'menu.html',context={'game':gaming})

def Cooking_profile(request):
    Cooking = 'Cooking'
    print(Cooking)
    return render(request,'menu.html',context={'cook':Cooking})

def Stream_profile(request):
    stream = 'streaming'
    print(stream)
    return render(request,'menu.html',context={'stream':stream})

def Social_profile(request):
    social = 'social'
    print(social)
    return render(request,'menu.html',context={'social':social})
def menu(request):
    return render(request, 'menu.html')


