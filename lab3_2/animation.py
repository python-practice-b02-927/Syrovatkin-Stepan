import graphics as gr
from math import sqrt
                                                                              
win = gr.GraphWin("Jenkslex and Ganzz project", 800, 1000)
win.setBackground('purple')

coords=gr.Point(200, 200)
velocity=gr.Point(2,7)

x0 = 400
y0 = 325

def draw_sphere():
    sphere = gr.Circle(gr.Point(x0, y0), 275)
    sphere.setFill('red')
    sphere.setOutline('yellow')
    sphere.draw(win)
    sphere.setWidth(15)

def draw_ball():
    circle = gr.Circle(coords, 15)
    circle.setFill('aqua')
    circle.draw(win)
    return circle

def ball_move(circle):
    circle.move(velocity.x, velocity.y)

def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point    

def r(x,y):
    radius_vector = gr.Point((x0-x) / 275, (y0-y) / 275)
    return r_vector

def n(x,y):
    normal_vector = gr.Point((x0-x) / 275, (y0-y) / 275)
    return r_vector

def scalar_multiplication(vector_1, vector_2):
    scalar = vector_1.x*vector_2.x + vector_1.y*vector_2.y
    return scalar

def velocity_changing(velocity, x, y):
    
    return velocity

def condition(velocity, x, y):
    if (x0-x)**2 + (y0-y)**2 >= 250**2:
        velocity = velocity_changing(velocity, x, y)
        
    return velocity

draw_sphere()
circle = draw_ball()

while True:
	
    ball_move(circle)
    coords=add(coords, velocity)
     
    x=coords.x
    y=coords.y
    velocity = condition(velocity, x, y)
    
    gr.time.sleep(0.02)
    
win.getMouse()
win.close
