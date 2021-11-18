from pico2d import *
import game_world
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Fountain:
    def __init__(self):
        self.image = load_image('Overworld.png')
        self.frame = 352
        self.x, self.y = 400, 350

    def get_bb(self):
        return self.x - 24, self.y - 6, self.x + 24, self.y + 18

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def draw(self):#352
        self.image.clip_draw(int(self.frame) * 48 + 352, 384, 48, 48, self.x, self.y)
        # draw_rectangle(*self.get_bb())