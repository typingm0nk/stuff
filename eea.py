#!/usr/bin/env python

def q(a,b):
    r=a%b
    q=a//b
    while r>1:
        a=b
        b=r
        q=a//b
        r=a%b
        print(a," = ",q,"*",b," + ",r)
    if r==1:
        return q
    else:
        False

def eea(m,e):
    if m==0 or e==0 or e>m: #check if input is correct
        return False
    x=q(m,e)
    d=(x*m+1)//e
    return(d)

def check(d,e,m):
    r = d*e %m
    if r==1:
        return True
    else:
        return False

e=2**16+1
m=173405
d=eea(m,e)
print(d,e,m)
print(check(d,e,m))
