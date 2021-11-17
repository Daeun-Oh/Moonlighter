from pico2d import *

class Monster1: # 나무 몬스터
    def __init__(self):
        self.image = load_image('log.png')
        self.x, self.y = randint(0, 800), randint(0, 600)

    global player
    def update(self):
        dist = (player.x - self.x)**2 + (player.y - self.y)**2
        if dist < 100**2:
            self.x = (1 - 0.1) * self.x + 0.1 * player.x
            self.y = (1 - 0.1) * self.y + 0.1 * player.y

    def draw(self):
        self.image.clip_draw(0, 32*3, 32, 32, self.x, self.y)