import game_framework
import main_state
from pico2d import *


name = "LoadingState"
image = None
logo_time = 0.0

go_where = -1 	# 0 - go to dungeon / 1 - go to map

def enter():
	print("Loading")
	global image
	image = load_image('loading.png')

def exit():
	global image
	del(image)

def update():
	global logo_time, go_where

	if (logo_time > 1.0):
		logo_time = 0
		go_where = 0
		game_framework.change_state(main_state)
	delay(0.01)
	logo_time += 0.01

def draw():
	global image
	clear_canvas()
	image.draw(400, 300)
	update_canvas()

def handle_events():
	events = get_events()

def pause(): pass

def resume(): pass