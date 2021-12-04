from pico2d import *
import main_state as m
import random

import server

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Monster2: # 작은 슬라임
    def __init__(self):
        self.image = load_image('frame1-mini.png')
        self.x, self.y = random.randint(400, 800 - 25), random.randint(0, 300)

    global player
    def update(self):
        dist = (server.player.x - self.x)**2 + (server.player.y - self.y)**2
        # if dist < 100**2:
        #     self.x = (1 - 0.1) * self.x + 0.1 * player.x
        #     self.y = (1 - 0.1) * self.y + 0.1 * player.y

    def draw(self):
        self.image.draw(self.x, self.y)