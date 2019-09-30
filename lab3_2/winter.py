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

	window1=gr.Rectangle(gr.Point(240,550), gr.Point(280,575))
	window1.setOutline(gr.color_rgb(240,250,250))
	window1.setFill(gr.color_rgb(240,250,250))
	window1.draw(win)

	window2=gr.Rectangle(gr.Point(300,550), gr.Point(340,575))
	window2.setOutline(gr.color_rgb(240,250,250))
	window2.setFill(gr.color_rgb(240,250,250))
	window2.draw(win)

	draw_wheel(210, 595, 250, 625)
	draw_wheel(330, 595, 370, 625)

	draw_smoke(80, 580, 150, 610)
	draw_smoke(50, 540, 120, 570)
	draw_smoke(20, 500, 90, 530)
	
	
	
	
def draw_buildingsandclouds(win):
	
	cloud1=gr.Oval(gr.Point(-60,80), gr.Point(400,150))
	cloud1.setOutline(gr.color_rgb(245,245,245))
	cloud1.setFill(gr.color_rgb(245,245,245))
	cloud1.draw(win)
	
	build1=gr.Rectangle(gr.Point(20,20), gr.Point(150,465))
	build1.setOutline(gr.color_rgb(170,170,170))
	build1.setFill(gr.color_rgb(170,170,170))
	build1.draw(win)
	
	cloud2=gr.Oval(gr.Point(-60,350), gr.Point(250,400))
	cloud2.setOutline(gr.color_rgb(100,100,130))
	cloud2.setFill(gr.color_rgb(100,100,130))
	cloud2.draw(win)
	
	build2=gr.Rectangle(gr.Point(160,60), gr.Point(290,475))
	build2.setOutline(gr.color_rgb(138,168,191))
	build2.setFill(gr.color_rgb(138,168,191))
	build2.draw(win)
	
	build3=gr.Rectangle(gr.Point(100,120), gr.Point(230,525))
	build3.setOutline(gr.color_rgb(230,230,230))
	build3.setFill(gr.color_rgb(230,230,230))
	build3.draw(win)
	
	build4=gr.Rectangle(gr.Point(450,20), gr.Point(580,465))
	build4.setOutline(gr.color_rgb(167,188,203))
	build4.setFill(gr.color_rgb(167,188,203))
	build4.draw(win)
	
	cloud3=gr.Oval(gr.Point(250,-20), gr.Point(650,80))
	cloud3.setOutline(gr.color_rgb(240,240,240))
	cloud3.setFill(gr.color_rgb(240,240,240))
	cloud3.draw(win)
	
	build5=gr.Rectangle(gr.Point(380,140), gr.Point(510,545))
	build5.setOutline(gr.color_rgb(120,140,150))
	build5.setFill(gr.color_rgb(120,140,150))
	build5.draw(win)
	
	cloud4=gr.Oval(gr.Point(250,300), gr.Point(650,360))
	cloud4.setOutline(gr.color_rgb(215,215,215))
	cloud4.setFill(gr.color_rgb(230,230,230))
	cloud4.draw(win)
	
	
	
	
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
