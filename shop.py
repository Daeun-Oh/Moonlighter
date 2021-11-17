from pico2d import *

class Shop:
    def __init__(self):
        self.image = load_image('Overworld.png')

    def draw(self):
        self.image.clip_draw(288, 120, 80, 100, 300, 300)