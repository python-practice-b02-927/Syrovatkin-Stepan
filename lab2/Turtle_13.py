import turtle as t

t.shape('turtle')


def duga(r):
    for i in range(25):
        t.forward(r)
        t.right(360/50)


def circle(r):
    for i in range(50):
        t.forward(r)
        t.right(360/50)


def eye():
	t.pendown()
	t.color('black','blue')
	t.begin_fill()
	circle(1.25)
	t.end_fill()
	t.penup()


t.color('black','yellow')
t.begin_fill()
circle(8)
t.end_fill()
t.penup()
t.goto(-20,-25)
eye()
t.goto(20,-25)
eye()
t.goto(0,-50)
t.right(90)
t.pendown()
t.pensize(8)
t.forward(20)
t.penup()
t.goto(40,-60)
t.pendown()
t.color('red')
duga(5)



