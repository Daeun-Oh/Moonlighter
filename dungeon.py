from pico2d import *

class Dungeon:
    def __init__(self):
        print("Dungeon")
        self.image = load_image('dungeon_tiles.png')

    def update(self):
        pass

    def draw(self):
        x, y, cnt = 0, 0, 0
        while y < 10:
            while x <= 12:
                self.image.clip_draw(40, 280, 64, 64, x * 64, y * 64)
                x += 1
            y += 1
            x = 0

    def get_bb(self):
        pass