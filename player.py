import game_framework
from pico2d import *

import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.8)  # 10 pixel 80 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6



# Player Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_DOWN, DOWN_DOWN, UP_UP, DOWN_UP, ENTER_DOWN, ENTER_UP = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,

    (SDL_KEYDOWN, SDLK_x): ENTER_DOWN,
    (SDL_KEYUP, SDLK_x): ENTER_UP
}


# Player States

class IdleState:

    def enter(player, event):
        # print("IdleState Entered")
        if event == RIGHT_DOWN:
            player.velocity_lr += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity_lr -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            player.velocity_ud += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            player.velocity_ud -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            player.velocity_lr -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity_lr += RUN_SPEED_PPS
        elif event == UP_UP:
            player.velocity_ud -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            player.velocity_ud += RUN_SPEED_PPS

        # player.timer = 1000

    def exit(player, event):
        # if event == SPACE:
        #     player.fire_ball()
        pass

    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        # player.timer -= 1
        # if player.timer == 0:
        #     player.add_event(SLEEP_TIMER)

    def draw(player):
        # print("IdleState Drawing")
        player.image.clip_draw(int(player.frame) * 16, 224, 16, 32, player.x, player.y)


class RunState:

    def enter(player, event):
        # print("RunState Entered")
        if event == RIGHT_DOWN:
            player.velocity_lr += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity_lr -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            player.velocity_ud += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            player.velocity_ud -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            player.velocity_lr -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity_lr += RUN_SPEED_PPS
        elif event == UP_UP:
            player.velocity_ud -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            player.velocity_ud += RUN_SPEED_PPS
        player.dir_lr, player.dir_ud = clamp(-1, player.velocity_lr, 1), clamp(-1, player.velocity_ud, 1)

    def exit(player, event):
        pass
#         # if event == SPACE:
#         #     player.fire_ball()

    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        player.x += player.velocity_lr * game_framework.frame_time
        player.y += player.velocity_ud * game_framework.frame_time
        player.x = clamp(25, player.x, 800 - 25)
        player.y = clamp(25, player.y, 600 - 25)

    def draw(player):
        # print("RunState Drawing")
        if player.dir_lr == 1:      # 오른쪽
            player.image.clip_draw(int(player.frame) * 16, 192, 16, 32, player.x, player.y)
        elif player.dir_lr == -1:   # 왼쪽
            player.image.clip_draw(int(player.frame) * 16, 128, 16, 32, player.x, player.y)
        elif player.dir_ud == 1:    # 위
            player.image.clip_draw(int(player.frame) * 16, 160, 16, 32, player.x, player.y)
        elif player.dir_ud == -1:   # 아래
            player.image.clip_draw(int(player.frame) * 16, 224, 16, 32, player.x, player.y)
        # else:
        #     player.image.clip_draw(int(player.frame) * 16, 224, 16, 32, player.x, player.y)


class AttackState:

    def enter(player, event):
        print("AttackState Entered")
        if event == RIGHT_DOWN:
            player.velocity_lr += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity_lr -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            player.velocity_ud += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            player.velocity_ud -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            player.velocity_lr -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity_lr += RUN_SPEED_PPS
        elif event == UP_UP:
            player.velocity_ud -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            player.velocity_ud += RUN_SPEED_PPS
        # player.dir_lr, player.dir_ud = clamp(-1, player.velocity_lr, 1), clamp(-1, player.velocity_ud, 1)

    def exit(player, event):
        pass
#         # if event == SPACE:
#         #     player.fire_ball()

    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        player.x += player.velocity_lr * game_framework.frame_time
        player.y += player.velocity_ud * game_framework.frame_time
        player.x = clamp(25, player.x, 800 - 25)
        player.y = clamp(25, player.y, 600 - 25)

    def draw(player):
        # print("RunState Drawing")
        if player.dir_lr == 1:      # 오른쪽
            player.image.clip_draw(int(player.frame) * 32, 32, 32, 32, player.x, player.y)
        elif player.dir_lr == -1:   # 왼쪽
            player.image.clip_draw(int(player.frame) * 32, 0, 32, 32, player.x, player.y)
        elif player.dir_ud == 1:    # 위
            player.image.clip_draw(int(player.frame) * 32, 64, 32, 32, player.x, player.y)
        elif player.dir_ud == -1:   # 아래
            player.image.clip_draw(int(player.frame) * 32, 96, 32, 32, player.x, player.y)
        # else:
        #     player.image.clip_draw(int(player.frame) * 16, 224, 16, 32, player.x, player.y)


# class SleepState:

#     def enter(boy, event):
#         boy.frame = 0

#     def exit(boy, event):
#         pass

#     def do(boy):
#         boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

#     def draw(boy):
#         if boy.dir == 1:
#             boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
#         else:
#             boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)






next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, UP_UP: RunState, DOWN_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState, ENTER_DOWN: AttackState, ENTER_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP: IdleState, DOWN_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, ENTER_DOWN: AttackState, ENTER_UP: RunState},
    AttackState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP: IdleState, DOWN_UP: IdleState, RIGHT_DOWN: AttackState, LEFT_DOWN: AttackState, UP_DOWN: AttackState, DOWN_DOWN: AttackState, ENTER_UP: IdleState}
    # SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}

# dir_lr = 0 # -1: left, +1: right
# dir_ud = 0 # -1: down, +1: up

class Player:
    def __init__(self):
        self.image = load_image('character.png')
        self.x, self.y = 400, 300
        self.frame = 0
        self.event_que = []
        self.dir_lr, self.dir_ud = 1, -1
        self.velocity_lr, self.velocity_ud = 0, 0
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 8, self.y - 16, self.x + 8, self.y + 16


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        # self.x += dir_lr * 3
        # self.y += dir_ud * 3
        # self.frame = (self.frame + 1) % 4

    def draw(self):
        self.cur_state.draw(self)
        # draw_rectangle(*self.get_bb())
        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #fill here
        # draw_rectangle(*self.get_bb())
        # self.image.clip_draw(self.frame * 16, 230, 16, 30, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        # global running
        # global player
        # global dir_lr, dir_ud
        # events = get_events()
        # for event in events:
        #     if event.type == SDL_QUIT:
        #         running = False
        #     elif event.type == SDL_KEYDOWN:
        #         if event.key == SDLK_RIGHT:
        #             dir_lr += 1
        #         elif event.key == SDLK_LEFT:
        #             dir_lr -= 1
        #         elif event.key == SDLK_UP:
        #             dir_ud += 1
        #         elif event.key == SDLK_DOWN:
        #             dir_ud -= 1
        #         elif event.key == SDLK_ESCAPE:
        #             running = False
        #     elif event.type == SDL_KEYUP:
        #         if event.key == SDLK_RIGHT:
        #             dir_lr -= 1
        #         elif event.key == SDLK_LEFT:
        #             dir_lr += 1
        #         elif event.key == SDLK_UP:
        #             dir_ud -= 1
        #         elif event.key == SDLK_DOWN:
        #             dir_ud += 1