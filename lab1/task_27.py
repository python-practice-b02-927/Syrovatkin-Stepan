#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
	move_right() 
	n=1
	while True:
		if wall_is_on_the_right():
			break
		fill_cell()
		for i in range(n):
			if wall_is_on_the_right():
				break
			move_right()

		n+=1
	


if __name__ == '__main__':
    run_tasks()
