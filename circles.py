#!/usr/bin/env python
from math import cos,sin,radians
from tkinter import *
import random

def circle(canvas,x,y, r,color):
    id = canvas.create_oval(x-r,y-r,x+r,y+r,outline=color)
    return id

canvas_width = 550
canvas_height= 550
master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)

w.pack()


def draw():
    w.delete("all")
    n=int(eval(ent.get()))
    R=360/n
    D=100

    for i in range(n):
        #color="#%06x" % random.randint(0, 0xFFFFFF)
        color="black"
        al=radians(i*R)
        x=D*cos(al)+300
        y=D*sin(al)+300
        circle(w,x,y,110,color)


ent = Entry(master)
ent.insert(0,"3")
btn = Button(master, text="Kreise",command=draw)

ent.pack()
btn.pack()
mainloop()
