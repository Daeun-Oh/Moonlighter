from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('Overworld.png')

    def update(self):
        pass

    def draw(self):
        x, y, cnt = 0, 0, 0
        while y <= 600:
            while x <= 800:
                self.image.clip_draw(0, 560, 10, 10, x % 800, y)
                x += 10
            y += 10
            x = 0

    def get_bb(self):
        pass