from pico2d import *
from random import *
from player import Player
from grass import Grass

class Tree:
    def __init__(self):
        self.image = load_image('Overworld.png')

    def draw(self):
        self.image.clip_draw(80, 288, 32, 40, 100, 100)
        self.image.clip_draw(80, 288, 32, 40, 300, 40)
        self.image.clip_draw(80, 288, 32, 40, 380, 80)

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

class Shop:
    def __init__(self):
        self.image = load_image('Overworld.png')

    def draw(self):
        self.image.clip_draw(288, 120, 80, 100, 300, 300)

class Portal:
    def __init__(self):
        self.image = load_image('purple_portal_sprite_sheet.png')
        self.frame = 0

    global dir_lr, dir_ud
    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*(512//8), (192//3)*2, 512//8, 192//3, 50, 400)

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


open_canvas()

grass = Grass()
tree = Tree()
fountain = Fountain()
shop = Shop()
portal = Portal()
player = Player()
monster1 = Monster1()
monster2 = Monster2()

running = True

dir_lr = 0 # -1: left, +1: right
dir_ud = 0 # -1: down, +1: up

while running:
    handle_events()
    portal.update()
    fountain.update()
    player.update()
    monster1.update()
    monster2.update()


    clear_canvas()
    grass.draw()
    portal.draw()
    player.draw()
    monster1.draw()
    monster2.draw()
    shop.draw()
    tree.draw()
    fountain.draw()

    update_canvas()


    delay(0.05)