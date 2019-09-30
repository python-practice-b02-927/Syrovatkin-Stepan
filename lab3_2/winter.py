import graphics as gr

win = gr.GraphWin("Jenkslex and Ganzz project", 600, 800)

def draw_smoke(x1, y1, x2, y2):
    smoke=gr.Oval(gr.Point(x1, y1), gr.Point(x2, y2))
    smoke.setOutline(gr.color_rgb(230,230,230))
    smoke.setFill(gr.color_rgb(230,230,230))
    smoke.draw(win)

def draw_wheel(x1, y1, x2, y2):
    wheel=gr.Oval(gr.Point(x1, y1), gr.Point(x2, y2))
    wheel.setOutline(gr.color_rgb(0,0,0))
    wheel.setFill(gr.color_rgb(0,0,0))
    wheel.draw(win)

def draw_window(x1, y1, x2, y2):
    window=gr.Rectangle(gr.Point(x1, y1), gr.Point(x2, y2))
    window.setOutline(gr.color_rgb(240,250,250))
    window.setFill(gr.color_rgb(240,250,250))
    window.draw(win)

def draw_car(win):
    pipe=gr.Oval(gr.Point(160,595), gr.Point(320,605))
    pipe.setOutline(gr.color_rgb(0,0,0))
    pipe.setFill(gr.color_rgb(0,0,0))
    pipe.draw(win)

    body1=gr.Rectangle(gr.Point(180,570), gr.Point(400,610))
    body1.setOutline(gr.color_rgb(80,200,250))
    body1.setFill(gr.color_rgb(80,200,250))
    body1.draw(win)

    body2=gr.Rectangle(gr.Point(230,540), gr.Point(350,570))
    body2.setOutline(gr.color_rgb(80,200,250))
    body2.setFill(gr.color_rgb(80,200,250))
    body2.draw(win)

    draw_window(240, 550, 280, 575)
    draw_window(300, 550, 340, 575)

    draw_wheel(210, 595, 250, 625)
    draw_wheel(330, 595, 370, 625)

    draw_smoke(80, 580, 150, 610)
    draw_smoke(50, 540, 120, 570)
    draw_smoke(20, 500, 90, 530)

def draw_build(x1, y1, x2, y2, red, green, blue):
    build=gr.Rectangle(gr.Point(x1, y1), gr.Point(x2, y2))
    build.setOutline(gr.color_rgb(red, green, blue))
    build.setFill(gr.color_rgb(red, green, blue))
    build.draw(win)	

def draw_cloud(x1, y1, x2, y2, red, green, blue):
    cloud=gr.Oval(gr.Point(x1, y1), gr.Point(x2, y2))
    cloud.setOutline(gr.color_rgb(red, green, blue))
    cloud.setFill(gr.color_rgb(red, green, blue))
    cloud.draw(win)	

def draw_buildingsandclouds(win):
    draw_cloud(-60, 80, 400, 150, 245, 245, 245)
    draw_build(20, 20, 150, 465, 170, 170, 170)
    draw_cloud(-60, 350, 250, 400, 100, 100, 130)
    draw_build(160, 60, 290, 475, 138, 168, 191)
    draw_build(100, 120, 230, 525, 230, 230, 230)
    draw_build(450, 20, 580, 465, 167, 188, 203)
    draw_cloud(250, -20, 650, 80, 240, 240, 240)
    draw_build(380, 140, 510, 545, 120, 140, 150)
    draw_cloud(250, 300, 650, 360, 230, 230, 230)

def draw_background(win):
    """Draw sky and ground"""
    sky=gr.Rectangle(gr.Point(0,0), gr.Point(600,445))
    sky.setOutline(gr.color_rgb(210,210,210))
    sky.setFill(gr.color_rgb(210,210,210))
    sky.draw(win)

    ground=gr.Rectangle(gr.Point(0,450), gr.Point(600,1000))
    ground.setFill(gr.color_rgb(120,120,120))
    ground.setOutline(gr.color_rgb(120,120,120))
    ground.draw(win)

    puddle=gr.Oval(gr.Point(0,530), gr.Point(1000,1000))
    puddle.setFill(gr.color_rgb(190,190,200))
    puddle.setOutline(gr.color_rgb(190,190,200))
    puddle.draw(win)

def main(win):
    """Draws picture"""
    draw_background(win)
    draw_car(win)
    draw_buildingsandclouds(win)

main(win)
win.getMouse()
win.close
