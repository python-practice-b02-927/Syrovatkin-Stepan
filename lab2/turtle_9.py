import turtle as t
import math

t.shape('turtle')
p=15
r=50
delta=20
def poli(n):
	k=r*2*math.sin(math.pi/n)
	t.penup()
	t.forward(delta)
	t.pendown()
	t.left(180-(n-2)*90/n)
	for i in range(n):
		t.forward(k)
		t.left(360/n)
	t.right(180-(n-2)*90/n)
for i in range(p):
	poli(i+3)
	r+=delta
