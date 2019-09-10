import turtle
import math

turtle.shape('turtle')
r=20
t=0
x0=0
y0=0

for i in range(1000):
	x0=0.5*r*t-r*math.sin(t)
	y0=r-r*math.cos(t)
	turtle.goto(x0, y0)
	t+=0.2



