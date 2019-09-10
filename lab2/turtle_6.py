import turtle

turtle.shape('turtle')
r=100
n=18
for i in range(n):
	turtle.right(360/n)
	turtle.forward(r)
	turtle.stamp()
	turtle.left(180)
	turtle.forward(r)
	turtle.left(180)
