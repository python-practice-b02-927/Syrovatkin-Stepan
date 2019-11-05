from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
g = 9.81
all_points = 0
id_points = canv.create_text(30,30,text = all_points,font = '28')


class Ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 40
        self.vy = 40
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
        

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        self.x += self.vx
        self.y -= self.vy
        self.vy -= g/2
        if self.x + self.r>=800 :
            self.vx= -self.vx/2
            self.x -=10
        if self.x - self.r<= 0:
            self.vx= -self.vx/2
            self.x +=10
        if self.y + self.r>=600:
            self.vy = -self.vy/2
            self.vx = self.vx*0.75
            self.y = 599 - self.r/2
        self.set_coords()   
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x-obj.x)**2+(self.y-obj.y)**2)**0.5 <= self.r + obj.r:
            return True
        else:
            return False 


class Gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)
        self.x = 20
        self.y = 420 

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.x, self.y)
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, self.y,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move_down(self, event):
        if self.y < 480 :
            self.y +=1
            canv.coords(self.id, 20, self.y,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def move_up(self, event):
        if self.y > 150 :
            self.y -=1
            canv.coords(self.id, 20, self.y,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )
class Target():
    global all_points, id_points
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.new_target()
        self.vx=rnd(-4, 4)
        self.vy=rnd(-4, 4)

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global all_points, id_points
        canv.coords(self.id, -10, -10, -10, -10)
        all_points += points
        canv.itemconfig(id_points, text=all_points)
    def move_target(self, other):
        if self.x+self.vx>=780 or self.x+self.vx<=20:
            self.vx = -self.vx
        if self.y+self.vy>=550 or self.y+self.vy<=200:
            self.vy = -self.vy
        self.x = self.x+self.vx
        self.y = self.y+self.vy
        canv.delete(self, self.id)
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)


t1 = Target()
t2 = Target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet, all_points, id_points
    t1.new_target()
    t2.new_target()
    bullet = 0
    if balls:
        for i in range(len(balls)-1, -1, -1):
            canv.delete(balls[i].id)
            del balls[i]        
    balls = []
    canv.itemconfig(screen1, text='')
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    root.bind('<Up>', g1.move_up)
    root.bind('<Down>', g1.move_down)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while balls or t1.live or t2.live:
        if t1.live and t2.live:
            t2.move_target([t1, t2])
            t1.move_target([t1, t2])
        elif t1.live:
            t1.move_target([t1, t2])
        elif t2.live:
            t2.move_target([t1, t2])
        for b in balls:
            b.move()
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if (t1.live == 0) and (t2.live == 0):
                canv.bind('<Button-1>', '')
                root.bind('<Return>', new_game)
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов, press Enter')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()

root.mainloop()
