#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
	for i in range(6):
		move_right()
		while not wall_is_on_the_right():
			fill_cell()
			move_right()
		move_down()
		move_left()
		while not wall_is_on_the_left():
			fill_cell()
			move_left()
		move_down()
	move_right()

if __name__ == '__main__':
    run_tasks()
