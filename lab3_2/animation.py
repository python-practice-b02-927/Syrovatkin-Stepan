from math import sqrt

import graphics as gr


win = gr.GraphWin("Jenkslex and Ganzz project", 800, 1000)
win.setBackground('purple')

coords=gr.Point(200, 200)
velocity=gr.Point(2,5)
# x-coordinate of the cell centre
x0 = 400
# y-coordinate of the cell centre
y0 = 300 
# The radius of the ball
BALL_RADIUS  = 20
# The radius of the sphere containing the ball
CELL_RADIUS = 275
# The thickness of the wall of the cavern
WALL_THICKNESS = 15
# The effective radius of the area where the ball moves
EFFECTIVE_RADIUS = 250


def draw_sphere():
    sphere = gr.Circle(gr.Point(x0, y0), CELL_RADIUS)
    sphere.setFill('red')
    sphere.setOutline('yellow')
    sphere.draw(win)
    sphere.setWidth(WALL_THICKNESS)


def draw_ball():
    circle = gr.Circle(coords, BALL_RADIUS)
    circle.setFill('aqua')
    circle.draw(win)
    return circle


def ball_move(circle):
    circle.move(velocity.x, velocity.y)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point    


def get_r_vector(x,y):
    length_vector = sqrt((x0-x)**2 + (y0-y)**2)
    radius_vector = gr.Point((x0-x) / length_vector, (y0-y) / length_vector)
    return radius_vector


def get_normal(x,y):
    length_vector = sqrt((x0-x)**2 + (y0-y)**2)
    normal_vector = gr.Point((y0-y) / length_vector, -(x0-x) / length_vector)
    return normal_vector


def scalar_multiplication(vector_1, vector_2):
    scalar = vector_1.x*vector_2.x + vector_1.y*vector_2.y
    return scalar


def reflect_velocity(velocity, x, y):
    vel_normal_0 = gr.Point(get_r_vector(x,y).x 
                            * scalar_multiplication(get_r_vector(x,y),velocity), 
                            get_r_vector(x,y).y 
                            * scalar_multiplication(get_r_vector(x,y),velocity)
    )
    vel_tau = gr.Point(get_normal(x,y).x 
                       * scalar_multiplication(get_normal(x,y),velocity), 
                       get_normal(x,y).y 
                       * scalar_multiplication(get_normal(x,y),velocity)
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


def update_velocity(velocity, x, y):
    if (x0-x)**2 + (y0-y)**2 >= EFFECTIVE_RADIUS**2:
        velocity = reflect_velocity(velocity, x, y)
        
    return velocity


draw_sphere()
circle = draw_ball()

while True:

    ball_move(circle)
    coords = add(coords, velocity)
     
    x = coords.x
    y = coords.y
    velocity = update_velocity(velocity, x, y)

    gr.time.sleep(0.02)

win.getMouse()
win.close
