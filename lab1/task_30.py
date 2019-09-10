#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
	n=0
	k=0
	while not wall_is_on_the_right():
		move_right()
		n+=1
	while not wall_is_on_the_left():
		move_left()
	l=n-1
	for i in range(n//2):
		for p in range(n-1):
			if p==k or p==l and not wall_is_on_the_right():
				move_right()
			fill_cell()
			if not wall_is_on_the_right():
				move_right()
		while not wall_is_on_the_left():
			move_left()
		k+=1
		l=l-1
		move_down()
	while not wall_is_beneath():
		move_down()
	k=0
	l=n-1
	for i in range(n//2):
		for p in range(n-1):
			if p==k or p==l and not wall_is_on_the_right():
				move_right()
			fill_cell()
			if not wall_is_on_the_right():
				move_right()
		while not wall_is_on_the_left():
			move_left()
		k+=1
		l=l-1
		move_up()
	for p in range(n//2):
		fill_cell()
		if not wall_is_on_the_right():
			move_right()
	move_right()
	for p in range(n//2):
		fill_cell()
		if not wall_is_on_the_right():
			move_right()
	while not wall_is_beneath():
		move_down()
	while not wall_is_on_the_left():
			move_left()
if __name__ == '__main__':
    run_tasks()
