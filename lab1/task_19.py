#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
	while not wall_is_on_the_right() and wall_is_above():
		move_right()
	if not wall_is_above():
		move_outright()
	while not wall_is_on_the_left() and wall_is_above():
		move_left()
	if not wall_is_above():
		move_outleft()
	if wall_is_on_the_left() and wall_is_beneath():
		while not wall_is_on_the_right():
			move_right()
		stop()

def move_outright():
	while not wall_is_on_the_right():
		move_right()
	while not wall_is_above():
		move_up()
	while not wall_is_on_the_left():
		move_left()
	return
def move_outleft():
	while not wall_is_on_the_left():
		move_left()
	while not wall_is_above():
		move_up()
	return
def stop():
	return
if __name__ == '__main__':
    run_tasks()
