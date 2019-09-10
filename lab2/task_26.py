#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
	while True:
		a=0
		k=0
		move_right()
		fill_cell()
		for i in range(2):
			move_down()
			fill_cell()
		if wall_is_beneath():
			k=1
		move_up()
		move_right()
		if wall_is_on_the_right():
			a=1
		fill_cell()
		move_left(2)
		fill_cell()
		move_up()
		if a==1:
			move_left(4)
		move_right(4)
		if a==1:
			if k==1:
				move_left(36)
				break
			move_down(4)
			move_left(36)
if __name__ == '__main__':
    run_tasks()
