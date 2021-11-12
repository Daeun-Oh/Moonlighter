from pico2d import *


from player import Player
from grass import Grass

name = "MainState"

player = None

def enter():
	global player
	player = Player()
	grass = Grass()
	# here

def exit():
	# here

def pause():
	pass

def resume():
	pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player.handle_event(event)