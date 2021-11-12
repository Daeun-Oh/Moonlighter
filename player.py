from pico2d import *

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