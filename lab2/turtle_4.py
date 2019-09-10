import turtle

turtle.shape('turtle')
k=40
n=10
for p in range(n):
	for i in range(4):
		turtle.forward(k)
		turtle.left(90)
	turtle.penup()
	turtle.right(90)
	turtle.forward(10)
	turtle.right(90)
	turtle.forward(10)
	turtle.left(180)
	turtle.pendown()
	k+=20
	

