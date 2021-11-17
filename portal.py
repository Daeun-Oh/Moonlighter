import random
from pico2d import *
import game_world
import game_framework
# import main_state
# from main_state import player
# from main_state import portal

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# COLLIDE = 0
# # Portal Event
# event_table = {
#     (main_state.collide(player, portal)): COLLIDE
# }

checkCollideState = 0


class IdleState:

    def enter(portal, event):
        print("IdleState Entered")

    def exit(portal, event):
        pass

    def do(portal):
        portal.frame = (portal.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(portal):
        portal.image.clip_draw(int(portal.frame) * 64, 120, 64, 72, portal.x, portal.y) # 원래 - x: 50, y: 400
        # draw_rectangle(*portal.get_bb())

class CollideState:

    def enter(portal, event):
        portal.frame = 0

    def exit(portal, event):
        pass

    def do(portal):
        global checkCollideState

        if portal.frame > 20.0:
            checkCollideState = 1

        portal.frame = portal.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        print(portal.frame, checkCollideState)


    def draw(portal):
        portal.image.clip_draw(int(portal.frame) * 64, 0, 64, 72, portal.x, portal.y) # 원래 - x: 50, y: 400


# next_state_table = {
#     IdleState: {COLLIDE: CollideState},
#     CollideState: {COLLIDE: CollideState}
# }

class Portal:
    def __init__(self):
        self.image = load_image('purple_portal_sprite_sheet.png')
        self.x, self.y = random.randint(0, 800 - 1), random.randint(0, 600 - 1)
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        # self.checkDrawing = 0

    def get_bb(self):
        return self.x - 24, self.y - 32, self.x + 24, self.y + 32

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        # self.frame = (self.frame + 1) % 8

    def draw(self):
        global checkCollideState
        self.cur_state.draw(self)
        # self.image.clip_draw(int(self.frame) * 64, 120, 64, 72, self.x, self.y) # 원래 - x: 50, y: 400
        # draw_rectangle(*self.get_bb())
        # print(checkCollideState)
        # print("난 아직도 포탈을 그리고 있다.", self.checkDrawing)
        # self.checkDrawing += 1