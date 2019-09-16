import turtle as t
import math

t.shape('turtle')

def duga(r):
    for i in range(25):
        t.forward(r)
        t.right(360/50)


t.penup()
t.backward(200)
t.pendown()
t.left(90)
for i in range(10):
    duga(8)
    duga(2)


