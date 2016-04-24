#!/usr/bin/env python
# -*- coding: cp1252 -*-

def d(a,b):
    v=0
    t=1
    while b>0:
        r=a%b
        q=a//b
        a=b
        b=r
        vv=t
        t=v-q*t
        v=vv
    return(v)

def eea(m,e):
    if m==0 or e==0 or e>m: #check if input is correct
        return False
    return(d(m,e))

def check(d,e,m):
    r = (d*e) %m
    if r==1:
        return True
    else:
        return ("ups, something went wrong.",d,e,m)

def teilerfremd(a,b):
    r=2
    while r>1:
        r=a%b
        if r==1:
            return True
        a=b
        b=r
    return False

m=12345678901234567890
e=2**16+1
if teilerfremd(e,m):
    d=eea(m,e)
    while d<0: #assuming we prefer a positiv d
        d+=m
    print(d,e,m)
    print(check(d,e,m))
else:
    print("e und m müssen teilerfremd sein")
