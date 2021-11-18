from pico2d import *
import main_state as m
import random

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Monster1: # 나무 몬스터
    def __init__(self):
        self.image = load_image('log.png')
        self.x, self.y = random.randint(400, 800 - 25), random.randint(300, 600 - 25)

    global player
    def update(self):
        dist = (m.player.x - self.x)**2 + (m.player.y - self.y)**2
        # if dist < 100**2:
        #     self.x = (1 - 0.8) * self.x + 0.8 * m.player.x  # 0.1
        #     self.y = (1 - 0.8) * self.y + 0.8 * m.player.y

    def draw(self):
        self.image.clip_draw(0, 32*3, 32, 32, self.x, self.y)