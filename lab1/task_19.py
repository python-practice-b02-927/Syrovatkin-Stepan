#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
	move_outtoright()
	move_outtoleft()
	if wall_is_beneath():
		while not wall_is_on_the_right():
			move_right()
		

def move_outtoright():
	while not wall_is_on_the_right():
		move_right()
	while not wall_is_above():
		move_up()
	while not wall_is_on_the_left():
		move_left()
	

def move_outtoleft():
	while not wall_is_on_the_left():
		move_left()
	while not wall_is_above():
		move_up()
	

if __name__ == '__main__':
    run_tasks()
