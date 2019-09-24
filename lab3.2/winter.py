import graphics as gr

win = gr.GraphWin("Jenkslex and Ganzz project", 600, 800)

def draw_car(win):
	pass
def draw_buildings(win):
	build1=gr.Rectangle(gr.Point(20,20), gr.Point(150,465))
	build1.setOutline(gr.color_rgb(170,170,170))
	build1.setFill(gr.color_rgb(170,170,170))
	build1.draw(win)
	
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
	
	build5=gr.Rectangle(gr.Point(380,140), gr.Point(510,545))
	build5.setOutline(gr.color_rgb(120,140,150))
	build5.setFill(gr.color_rgb(120,140,150))
	build5.draw(win)
def draw_clouds(win):
	pass
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
	
	
	
def main(win):
	"""Draws picture"""
	draw_background(win)
	draw_car(win)
	draw_buildings(win)
	draw_clouds(win)
	
	



main(win)
win.getMouse()
win.close
