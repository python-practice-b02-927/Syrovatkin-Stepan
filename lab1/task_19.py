#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
	while not wall_is_on_the_left():
		move_left()
	if not wall_is_beneath():
		move_out()
	while not wall_is_on_the_right():
		move_right()
	if not wall_is_beneath():
		move_out()
		

def move_out():
	while not wall_is_above():
		move_up()
	while not wall_is_on_the_left():
		move_left()
	return

	

if __name__ == '__main__':
    run_tasks()
