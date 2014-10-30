#!/usr/bin/env python
from math import *


#basic tasten
l5=['q','a','y','1','2']            #a
l4=['w','s','x','3']                #s
l3=['e','d','c','4']                #d
l2=['r','f','v','t','g','b','5','6']#f

r5=['p']                            #ö
r4=['0','l','o']                    #l
r3=['i','k','9']                    #k
r2=['z','h','n','u','j','m','7','8']#j

#zurückgelegte distanzen. annahme der tippende finger kehrt zwischen zwei anschlägen immer zur ruhestellung zurück.

e1=2*sqrt(0.25*0.25 + 2*2)  #2,3,4,5,8,9,0
e2=2*sqrt(1.25*1.25 + 2*2)  #6
e3=2*sqrt(0.75*0.75 + 2*2)  #1,7

d1=2*sqrt(0.25*0.25 + 1)    #q,w,e,r,u,i,o,p
d2=2*sqrt(0.75*0.75 +1)     #t
d3=2*sqrt(1.25*1.25 +1)     #z

b1=2*sqrt(0.5*0.5 + 1)      #y,x,c,v,n,m
b2=2*sqrt(1.5*1.5 + 1)      #b

c=2*1                       #g,h

dista={ x:e1 for x in ('2','3','4','5','8','9','0')}
dista['6']=e2
dista['1']=e3
dista['7']=e3
distb={y:d1 for y in ('q','w','e','r','u','i','o','p')}
distc={x:b1 for x in ('y','x','c','v','n','m')}
dista['t']=d2
dista['z']=d3
dista['b']=b2
dista['h']=c
dista['g']=c
dist= dict(list(dista.items()) + list(distb.items()) + list(distc.items()))

summe=0
with open('text.txt','r') as fil:
    text=fil.read()
    for line in text:
        for char in line.lower():
            if char in dist:
                summe+=dist[char]
    fil.close()
print(summe)

