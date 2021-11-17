import random
import json
import os

from pico2d import *
import game_framework
import game_world

from player import Player
from grass import Grass
from portal import Portal

name = "MainState"

player = None
grass = None
portal = None


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True




def enter():
    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global player
    player = Player()
    game_world.add_object(player, 1)

    global portal
    portal = Portal()
    game_world.add_object(portal, 2)





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