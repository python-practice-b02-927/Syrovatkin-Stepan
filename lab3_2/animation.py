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

def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('aqua')
    circle.draw(win)


def add(point_1, point_2):
    new_point = Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point    
        
def main(win):
    draw_sphere()
    draw_ball(coords)

main(win)    
win.getMouse()
win.close
