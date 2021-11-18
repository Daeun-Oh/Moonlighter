from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('Overworld.png')

    def get_bb(self):
        pass

    def update(self):
        pass

    def draw(self):
        x, y, cnt = 0, 0, 0
        while y <= 60:
            while x <= 80:
                self.image.clip_draw(0, 560, 10, 10, x * 10, y * 10)
                x += 1
            y += 1
            x = 0

class RaisedGrass:
    def __init__(self):
        self.image = load_image('Overworld.png')
        self.x, self.y = 48, 500

    def get_bb(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(64, 328, 48, 104, self.x, self.y)