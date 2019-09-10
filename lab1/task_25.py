#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
	while True:
		move_right()
		for i in range(3):
			move_down()
			fill_cell()
		move_up()
		move_right()
		if wall_is_on_the_right():
			fill_cell()
			move_left(2)
			fill_cell()
			move_up()
			break	
		fill_cell()
		move_left(2)
		fill_cell()
		move_up(2)
		move_right(4)
if __name__ == '__main__':
    run_tasks()
