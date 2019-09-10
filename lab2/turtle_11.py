import turtle

turtle.shape('turtle')
n=100
k=10
turtle.left(90)
def circlel(n):
	for i in range(n):
		turtle.forward(3)
		turtle.left(360/n)
def circler(n):
	for i in range(n):
		turtle.forward(3)
		turtle.right(360/n)		
for i in range(k):
	circlel(n)
	circler(n)
	n+=50



