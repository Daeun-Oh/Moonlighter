import random
import json
import os

from pico2d import *
import game_framework
import game_world

from player import Player
from grass import Grass, RaisedGrass
from portal import Portal
from dungeon import Dungeon
from monster1 import Monster1
from monster2 import Monster2
from fountain import Fountain
from shop import Shop

# portal
import portal as p
from portal import CollideState

# loading
import loading_state

# dungeon



name = "MainState"

player = None
grass = None
raisedGrass = None
portal = None
dungeon = None
monster1 = None
monster2 = None
fountain = None
shop = None


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

        global raisedGrass
        raisedGrass = RaisedGrass()
        game_world.add_object(raisedGrass, 0)

        global fountain
        fountain = Fountain()
        game_world.add_object(fountain, 1)

        global shop
        shop = Shop()
        game_world.add_object(shop, 1)

        global portal
        portal = Portal()
        game_world.add_object(portal, 1)

    if loading_state.go_where == 0:
        game_world.remove_object(grass)
        game_world.remove_object(raisedGrass)
        game_world.remove_object(portal)
        game_world.remove_object(fountain)
        game_world.remove_object(shop)

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

    # 포탈 - 플레이어
    if collide(player, portal):
        # print("COLLISION")
        portal.cur_state = CollideState
    # print(p.checkCollideState)
    if p.checkCollideState == 1:
        game_world.remove_object(portal)
        p.checkCollideState = 2
        game_framework.change_state(loading_state)

    # 분수 - 플레이어
    if collide(player, fountain):
        if player.dir_lr == 1:      # 오른쪽
            player.x -= 2
        elif player.dir_lr == -1:   # 왼쪽
            player.x += 2
        elif player.dir_ud == 1:    # 위
            player.y -= 2
        elif player.dir_ud == -1:   # 아래
            player.y += 2

    # 상점 - 플레이어
    if collide(player, shop):
        if player.dir_lr == 1:      # 오른쪽
            player.x -= 2
        elif player.dir_lr == -1:   # 왼쪽
            player.x += 2
        elif player.dir_ud == 1:    # 위
            player.y -= 2
        elif player.dir_ud == -1:   # 아래
            player.y += 2

    


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()