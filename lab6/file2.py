from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
l = Label(root, bg='black', fg='white', width=20)
l.pack()
canv.pack(fill=BOTH,expand=1)
i=0
k=0
m=1000
balls=[]


colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x, y, r, m
    #canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    vx = rnd(-5,5)
    vy = rnd(-5,5)
    id_ = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    ball={'id': id_, 'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy}
    balls.append(ball)
    root.after(m,new_ball)
    l['text'] = 'Score: ' + str(i)

def click(event):
    global i, m
    for k, b in enumerate(balls):   
        if (event.x-b['x'])**2 + (event.y-b['y'])**2 <= b['r']**2:
            i+=2
            canv.delete(b['id'])
            del balls[k]
            if m>=300:
                m-=10
    i-=1
    print('click')

   
        
new_ball()

canv.bind('<Button-1>', click)
mainloop()
