from pico2d import *

class Tree:
    def __init__(self):
        self.image = load_image('Overworld.png')

    def draw(self):
        self.image.clip_draw(80, 288, 32, 40, 100, 100)
        self.image.clip_draw(80, 288, 32, 40, 300, 40)
        self.image.clip_draw(80, 288, 32, 40, 380, 80)