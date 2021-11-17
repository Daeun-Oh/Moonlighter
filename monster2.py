from pico2d import *

class Monster2: # 작은 슬라임
    def __init__(self):
        self.image = load_image('frame1-mini.png')
        self.x, self.y = randint(0, 800), randint(0, 600)

    global player
    def update(self):
        dist = (player.x - self.x)**2 + (player.y - self.y)**2
        if dist < 100**2:
            self.x = (1 - 0.1) * self.x + 0.1 * player.x
            self.y = (1 - 0.1) * self.y + 0.1 * player.y

    def draw(self):
        self.image.draw(self.x, self.y)