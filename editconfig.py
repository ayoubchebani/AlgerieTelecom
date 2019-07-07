#!/usr/bin/env python
import re
gaclname = ""
gpassparams = ""
gredirectlink = ""

def getaclname(aclname):
    return aclname

def getpassparams(passparams):
    return passparams

def getredirectlink(redirectlink):
    return redirectlink

def getvalues(aclname, passparams, redirectlink):
    aclname = getaclname(aclname)
    passparams = getpassparams(passparams)
    redirectlink = getredirectlink(redirectlink)

    return aclname,passparams, redirectlink


def changeme(matchObj):
	m = matchObj.group(0)
        if "acl" in m:
            return "acl %s"%gaclname
        elif "default" in m:
            return m
        elif "pass" in m:
            return "pass %s all"%gpassparams
        elif "redirect" in m:
            return "redirect %s"%gredirectlink
        else: 
            return 


def editconfig(filecontent, aclname,passparams,redirectlink):
    aclname,passparams,redirectlink =  getvalues(aclname, passparams, redirectlink)

    global gaclname,gpassparams, gredirectlink
    gaclname = aclname
    gpassparams = passparams
    gredirectlink = redirectlink

    return re.sub("acl*.*\S+ |default*.* |pass*.*|redirect*.*", changeme, filecontent, flags=re.MULTILINE)

#f = open("origin.conf","r").read()

#print editconfig(f, "game", '!game', "www.foo.bar")
#print editconfig(aclname, passparams, redirectlink)

