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

import server

# portal
from portal import CollideState

# loading
import loading_state




name = "MainState"



def enter():
    if loading_state.go_where == -1 or loading_state.go_where == 1:
        server.grass = Grass()
        game_world.add_object(server.grass, 0)

        server.raisedGrass = RaisedGrass()
        game_world.add_object(server.raisedGrass, 0)

        server.fountain = Fountain()
        game_world.add_object(server.fountain, 1)

        server.shop = Shop()
        game_world.add_object(server.shop, 1)

        server.portal = Portal()
        game_world.add_object(server.portal, 1)

    if loading_state.go_where == 0:
        game_world.remove_object(server.grass)
        game_world.remove_object(server.raisedGrass)
        game_world.remove_object(server.portal)
        game_world.remove_object(server.fountain)
        game_world.remove_object(server.shop)

        server.dungeon = Dungeon()
        game_world.add_object(server.dungeon, 0)

        server.monster1 = Monster1()
        game_world.add_object(server.monster1, 1)

        server.monster2 = Monster2()
        game_world.add_object(server.monster2, 1)

    server.player = Player()
    game_world.add_object(server.player, 1)





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
            server.player.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


    # # 상점 - 플레이어
    # if collide(player, shop):
    #     if player.dir_lr == 1:      # 오른쪽
    #         player.x -= 2
    #     elif player.dir_lr == -1:   # 왼쪽
    #         player.x += 2
    #     elif player.dir_ud == 1:    # 위
    #         player.y -= 2
    #     elif player.dir_ud == -1:   # 아래
    #         player.y += 2

    # # 몬스터1 - 플레이어
    # if loading_state.go_where == 1 and collide(player, monster1):
    #     if player.cur_state == AttackState:
    #         monster1.HP -= 10
    


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()