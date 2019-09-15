#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
	for i in range(5):
		for j in range(10):
			krest()
		move_down(2)
		if not wall_is_beneath():
			move_down(2)
		move_left(38)
	

def krest():
	move_right()
	fill_cell()
	for i in range(2):
		move_down()
		fill_cell()
	move_up()
	move_right()
	fill_cell()
	move_left(2)
	fill_cell()
	move_up()
	move_right(2)
	if not wall_is_on_the_right():
		move_right(2)


if __name__ == '__main__':
    run_tasks()
