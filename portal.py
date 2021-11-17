import random
from pico2d import *
import game_world
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Portal:
    def __init__(self):
        self.image = load_image('purple_portal_sprite_sheet.png')
        self.x, self.y = random.randint(0, 800 - 1), random.randint(0, 600 - 1)
        self.frame = 0

    def get_bb(self):
        return self.x - 24, self.y - 32, self.x + 24, self.y + 32

    def draw(self):
        self.image.clip_draw(int(self.frame) * 64, 120, 64, 72, self.x, self.y) # 원래 - x: 50, y: 400
        draw_rectangle(*self.get_bb())

    def update(self):
        # self.frame = (self.frame + 1) % 8
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    