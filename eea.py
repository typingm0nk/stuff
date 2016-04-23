#!/usr/bin/env python

def q(aa,bb):
    a=0
    b=aa
    q=0
    u=0
    s=1
    v=1
    t=0
    print("a","b","q","u","s","v","t")
    print(a,b,q,u,s,v,t)
    a=aa
    b=bb
    q=a//b
    u=1
    s=0
    v=0
    t=1
    print(a,b,q,u,s,v,t)
    while b>0:
        r=a%b
        q=a//b
        a=b
        b=r
        if b==0:
            return q #TODO
        uu=s
        vv=t
        s=u-q*s
        t=v-q*t
        u=uu
        v=vv
        print(a,b,q,u,s,v,t)
    return(u)

def eea(m,e):
    if m==0 or e==0 or e>m: #check if input is correct
        return False
    return(q(m,e))

def check(d,e,m):
    r = (d*e) %m
    if r==1:
        return True
    else:
        return ("r:",r)

e=78
m=99
d=eea(m,e)
print(d,e,m)
print(check(d,e,m))
