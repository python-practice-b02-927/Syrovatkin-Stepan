#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
	move_down()
	n=13
	for i in range(13):
		move_right()
		for j in range(n):
			fill_cell()
			move_down()
		for k in range(n):
			move_up()
		move_down()
		n-=1
	while not wall_is_on_the_left():
		move_left()
	move_right()
if __name__ == '__main__':
    run_tasks()
