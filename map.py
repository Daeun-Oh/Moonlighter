from pico2d import *
from random import *

class Grass:
    def __init__(self):
        self.image = load_image('Overworld.png')

    def draw(self):
        x, y, cnt = 0, 0, 0
        while y <= 600:
            while x <= 800:
                self.image.clip_draw(0, 560, 10, 10, x % 800, y)
                x += 10
            y += 10
            x = 0

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


class Player:
    def __init__(self):
        self.image = load_image('character.png')
        self.x, self.y = 400, 300
        self.frame = 0


    global dir_lr, dir_ud
    def update(self):
        self.x += dir_lr * 3
        self.y += dir_ud * 3
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 16, 230, 16, 30, self.x, self.y)

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


def handle_events():
    global running
    global player
    global dir_lr, dir_ud
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_lr += 1
            elif event.key == SDLK_LEFT:
                dir_lr -= 1
            elif event.key == SDLK_UP:
                dir_ud += 1
            elif event.key == SDLK_DOWN:
                dir_ud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_lr -= 1
            elif event.key == SDLK_LEFT:
                dir_lr += 1
            elif event.key == SDLK_UP:
                dir_ud -= 1
            elif event.key == SDLK_DOWN:
                dir_ud += 1


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