#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
	move_virtically()
	move_horizontally()
	
	
def move_virtically():
	while not wall_is_above():
		move_up()
		
		
def move_horizontally():
	if wall_is_on_the_right():
		while not wall_is_on_the_left():
			move_left()
	elif wall_is_on_the_left():
		while not wall_is_on_the_right():
			move_right()


if __name__ == '__main__':
    run_tasks()
