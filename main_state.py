import random
import json
import os

from pico2d import *
import game_framework
import game_world

from player import Player
from grass import Grass
from portal import Portal
from dungeon import Dungeon
from monster1 import Monster1
from monster2 import Monster2

# portal
import portal as p
from portal import CollideState

# loading
import loading_state

# dungeon



name = "MainState"

player = None
grass = None
portal = None
dungeon = None
monster1 = None
monster2 = None


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True




def enter():
    if loading_state.go_where == -1 or loading_state.go_where == 1:
        global grass
        grass = Grass()
        game_world.add_object(grass, 0)

        global portal
        portal = Portal()
        game_world.add_object(portal, 1)

    if loading_state.go_where == 0:
        global dungeon
        dungeon = Dungeon()
        game_world.add_object(dungeon, 0)

        global monster1
        monster1 = Monster1()
        game_world.add_object(monster1, 1)

        global monster2
        monster2 = Monster2()
        game_world.add_object(monster2, 1)

    global player
    player = Player()
    game_world.add_object(player, 1)





def exit():
    game_world.clear()

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


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if collide(player, portal):
        # print("COLLISION")
        portal.cur_state = CollideState
    # print(p.checkCollideState)
    if p.checkCollideState == 1:
        game_world.remove_object(portal)
        p.checkCollideState = 2
        game_framework.change_state(loading_state)

    # fill here for collision check
    # for ball in balls:
    #     if collide(boy, ball):
    #         if collide(boy, ball):
    #             # print("COLLISION")
    #             balls.remove(ball)  # 충돌을 검사해야 할 공 리스트(balls)에서 제거
    #             game_world.remove_object(ball)  # 게임 월드 내에서 제거

    # for ball in balls:
    #     if collide(grass, ball):
    #         ball.stop()

    # delay(0.9)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()