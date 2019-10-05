import graphics as gr
from math import sqrt
                                                                              
win = gr.GraphWin("Jenkslex and Ganzz project", 800, 1000)
win.setBackground('purple')

x0 = 400
y0 = 325

def draw_sphere():
    sphere = gr.Circle(gr.Point(x0, y0), 275)
    sphere.setFill('red')
    sphere.setOutline('yellow')
    sphere.draw(win)
    sphere.setWidth(15)
    
def main(win):
    draw_sphere()


main(win)    
win.getMouse()
win.close
