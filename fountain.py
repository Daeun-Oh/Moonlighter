from pico2d import *

class Fountain:
    def __init__(self):
        self.image = load_image('Overworld.png')
        self.frame = 352

    def update(self):
        if self.frame == 352 + 48*2:
            self.frame = 352
        else:
            self.frame += 48

    def draw(self):#352
        self.image.clip_draw(self.frame, 384, 48, 48, 450, 300)