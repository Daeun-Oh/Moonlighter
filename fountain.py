from pico2d import *
import game_world
import game_framework

import server
import collision

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

        if collision.collide(self, server.player):
            if server.player.dir_lr == 1:      # 오른쪽
                server.player.x = 400 - 24 - 2
            elif server.player.dir_lr == -1:   # 왼쪽
                server.player.x = 400 + 24 + 2
            elif server.player.dir_ud == 1:    # 위
                server.player.y = 400 - 6 - 2
            elif server.player.dir_ud == -1:   # 아래
                server.player.y = 400 + 18 + 2

    def draw(self):#352
        self.image.clip_draw(int(self.frame) * 48 + 352, 384, 48, 48, self.x, self.y)
        # draw_rectangle(*self.get_bb())