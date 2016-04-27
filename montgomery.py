#!/usr/bin/env python

def mm(a,b,rinv):
    return a*b*rinv

def c(a,r,rinv):
    return mm(a,r*r,rinv)

def d(a,rinv):
    return mm(a,1,rinv)

def inv(a,b):
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

#gesucht a**n mod m ohne teures div
r=1000

a=158
b=766
m=853

minv=inv(r,m)+r
print("minv: ",minv)
rinv=inv(m,r)
print("rinv: ",rinv)

t=a*b
print(t)
x=(t*minv*(-1))%r #TODO: mod ohne teuer machen
print(x)
t2=t+x*m
print(t2)
t3=t2//r
print(t3)
