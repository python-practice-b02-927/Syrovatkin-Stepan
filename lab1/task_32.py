#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
	n=0
	while wall_is_beneath():
		while not wall_is_above():
			move_up()
			if cell_is_filled():
				n+=1
		while not wall_is_beneath():
			move_down()
		move_right()
	while not wall_is_on_the_left():
		move_left()
	mov('ax',n)
	while wall_is_beneath():
		if wall_is_above() and wall_is_beneath():
			fill_cell()
		while not wall_is_above():
			move_up()
			if not cell_is_filled():
				fill_cell()
		while not wall_is_beneath():
			move_down()
		move_right()


if __name__ == '__main__':
    run_tasks()
