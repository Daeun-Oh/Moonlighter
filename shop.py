from pico2d import *

class Shop:
    def __init__(self):
        self.image = load_image('Overworld.png')
        self.x, self.y = 300, 300

    def get_bb(self):
        return self.x - 40, self.y - 16, self.x + 40, self.y + 24

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(288, 120, 80, 96, self.x, self.y)
        # draw_rectangle(*self.get_bb())