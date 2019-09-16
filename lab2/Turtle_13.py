import turtle as t
import math 
t.shape('turtle')


def duga(r):
    for i in range(180):
        t.right(1)
        t.forward(r*math.pi/180)


def circle(r):
    for i in range(360):
        t.right(1)
        t.forward(r*math.pi/180)

def eye():
	t.pendown()
	t.color('black','blue')
	t.begin_fill()
	circle(10)
	t.end_fill()
	t.penup()


t.color('black','yellow')
t.begin_fill()
circle(70)
t.end_fill()
t.penup()
t.goto(-25,-25)
eye()
t.goto(25,-25)
eye()
t.goto(0,-50)
t.right(90)
t.pendown()
t.pensize(8)
t.forward(20)
t.penup()
t.goto(50,-70)
t.pendown()
t.color('red')
duga(50)

input()

