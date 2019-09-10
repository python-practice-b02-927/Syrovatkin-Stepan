import turtle

turtle.shape('turtle')
n=100
fi=60
k=int(360/fi)
def circle(n):
	for i in range(n):
		turtle.forward(3)
		turtle.left(360/n)
for i in range(k):
	circle(n)
	turtle.left(fi)


