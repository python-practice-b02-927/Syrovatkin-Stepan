import graphics as gr
from math import sqrt
                                                                              
win = gr.GraphWin("Jenkslex and Ganzz project", 800, 1000)
win.setBackground('purple')

coords=gr.Point(200, 200)
velocity=gr.Point(2,3)

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
        
def main(win):
    draw_sphere()
    circle0 = draw_ball()
    while True:
        ball_move(circle0)
        
        global coords
        
        coords=add(coords, velocity)
        
        gr.time.sleep(0.02)

main(win)    
win.getMouse()
win.close
