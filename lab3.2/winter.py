import graphics as gr

win = gr.GraphWin("Jenkslex and Ganzz project", 600, 1000)

def draw_car(win):
	pass
def draw_buildings(win):
	pass
def draw_clouds(win):
	pass
def draw_background(win):
	"""Draw sky and ground"""
	sky=gr.Rectangle(gr.Point(0,0), gr.Point(600,495))
	sky.setFill('lightgrey')
	sky.draw(win)
	ground=gr.Rectangle(gr.Point(0,500), gr.Point(600,1000))
	ground.setFill('grey')
	ground.draw(win)
	
	
	
def main(win):
	"""Draws picture"""
	draw_car(win)
	draw_buildings(win)
	draw_clouds(win)
	draw_background(win)
	
	



main(win)
win.getMouse()
win.close
