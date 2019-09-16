import turtle as t
import math

t.shape('turtle')
k=75
n=11


def zv(n):
	for i in range(n):
		t.forward(k)
		t.right(180*(n-1)/n)

zv(11)
t.penup()
t.forward(3*k)
t.pendown()
zv(5)
