from pico2d import *

class Portal:
    def __init__(self):
        self.image = load_image('purple_portal_sprite_sheet.png')
        self.frame = 0

    global dir_lr, dir_ud
    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*(512//8), (192//3)*2, 512//8, 192//3, 50, 400)