from math import sqrt

import graphics as gr


win = gr.GraphWin("Jenkslex and Ganzz project", 800, 1000)
win.setBackground('purple')

coords=gr.Point(200, 200)
velocity=gr.Point(2,5)

x0 = 400
y0 = 300

def draw_sphere():
    sphere = gr.Circle(gr.Point(x0, y0), 275)
    sphere.setFill('red')
    sphere.setOutline('yellow')
    sphere.draw(win)
    sphere.setWidth(15)


def draw_ball():
    circle = gr.Circle(coords, 20)
    circle.setFill('aqua')
    circle.draw(win)
    return circle


def ball_move(circle):
    circle.move(velocity.x, velocity.y)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point    


def r(x,y):
    length_vector = sqrt((x0-x)**2 + (y0-y)**2)
    radius_vector = gr.Point((x0-x) / length_vector, (y0-y) / length_vector)
    return radius_vector


def n(x,y):
    length_vector = sqrt((x0-x)**2 + (y0-y)**2)
    normal_vector = gr.Point((y0-y) / length_vector, -(x0-x) / length_vector)
    return normal_vector


def scalar_multiplication(vector_1, vector_2):
    scalar = vector_1.x*vector_2.x + vector_1.y*vector_2.y
    return scalar


def velocity_changing(velocity, x, y):
    vel_normal_0 = gr.Point(r(x,y).x
                            *scalar_multiplication(r(x,y),velocity), 
                            r(x,y).y
                            *scalar_multiplication(r(x,y),velocity)
    )
    vel_tau = gr.Point(n(x,y).x
                       *scalar_multiplication(n(x,y),velocity), 
                       n(x,y).y
                       *scalar_multiplication(n(x,y),velocity)
    )
    vel_normal_1 = gr.Point(-vel_normal_0.x,-vel_normal_0.y)
    
    i = gr.Point(1, 0)
    j = gr.Point(0, 1)
    
    vel_1_x = scalar_multiplication(vel_normal_1, i)
    vel_2_x = scalar_multiplication(vel_tau, i)
    
    vel_1_y = scalar_multiplication(vel_normal_1, j)
    vel_2_y = scalar_multiplication(vel_tau, j)
    
    velocity = gr.Point(vel_1_x + vel_2_x, vel_1_y + vel_2_y) 
    
    return velocity


def condition(velocity, x, y):
    if (x0-x)**2 + (y0-y)**2 >= 250**2:
        velocity = velocity_changing(velocity, x, y)
        
    return velocity


draw_sphere()
circle = draw_ball()

while True:

    ball_move(circle)
    coords = add(coords, velocity)
     
    x = coords.x
    y = coords.y
    velocity = condition(velocity, x, y)

    gr.time.sleep(0.02)

win.getMouse()
win.close
