from pico2d import *
import main_state as m
import random
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

import math
import server

import game_world
from player import AttackState

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Monster1: # 나무 몬스터
    images = None

    def load_images(self):
        if Monster1.images == None:
            Monster1.image = load_image('log.png')

    def prepare_patrol_points(self):
        # fill here
        positions = [(400, 700), (400, 700), (400, 700), (400, 700), (400, 700), (400, 700), (400, 700), (400, 700)]
        # 좌표 획득시, 기준 위치가 왼쪽 위

        self.patrol_points = []
        for p in positions:
            self.patrol_points.append((p[0], 800-p[1]))    # pico2d 상의 좌표계를 이용하도록 변경.

        pass

    def __init__(self):
        # self.image = load_image('log.png')
        # self.x, self.y = random.randint(400, 800 - 25), random.randint(300, 600 - 25)
        self.HP = 200

        self.prepare_patrol_points()
        self.patrol_order = 1
        self.x, self.y = self.patrol_points[0]
        self.load_images()
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.timer = 1.0 # change direction every 1 sec when wandering
        self.wait_timer = 2.0
        self.frame = 0
        self.build_behavior_tree()

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 1.0
            self.dir = random.random() * 2 * math.pi # 방향을 라디안 값으로 설정.
            print('Wander Success')
            return BehaviorTree.SUCCESS
        return BehaviorTree.SUCCESS
        # else:
        #     return BehaviorTree.RUNNING
        # fill here
        pass


    def wait(self):
        self.speed = 0
        self.wait_timer -= game_framework.frame_time
        if self.wait_timer <= 0:
            self.wait_timer = 2.0
            print('Wait Success')
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        # fill here
        pass



    def find_player(self):
        # fill here
        distance2 = (server.player.x - self.x)**2 + (server.player.y - self.y)**2
        if distance2 <= (PIXEL_PER_METER*10)**2:
            print('Find Player Success')
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL

    def move_to_player(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        self.dir = math.atan2(server.player.y - self.y, server.player.x - self.x)
        return BehaviorTree.SUCCESS     # 일단, 소년 쪽으로 움직이기만 해도 성공으로 여긴다.

    def get_next_position(self):
        # fill here
        self.target_x, self.target_y = self.patrol_points[self.patrol_order % len(self.patrol_points)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        print('Next Position Found Success')
        return BehaviorTree.SUCCESS

    def move_to_target(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        distance2 = (self.target_x - self.x)**2 + (self.target_y - self.y)**2
        
        if distance2 < PIXEL_PER_METER**2:  # 거리가 1미터 이내이면
            print('Moved to Target Success')
            return BehaviorTree.SUCCESS     # 다 왔다.
        else:
            # print('Moving to Target')
            return BehaviorTree.RUNNING



    def build_behavior_tree(self):
        wander_node = LeafNode('Wander', self.wander)
        wait_node = LeafNode('Wait', self.wait)

        wander_wait_node = SequenceNode('WanderAndWait')
        wander_wait_node.add_children(wander_node, wait_node)

        get_next_position_node = LeafNode('Get Next Position', self.get_next_position)
        move_to_target_node = LeafNode('Move to Target', self.move_to_target)
        patrol_node = SequenceNode('Patrol')
        patrol_node.add_children(get_next_position_node, move_to_target_node)

        find_player_node = LeafNode('Find Player', self.find_player)
        move_to_player_node = LeafNode('Move to Player', self.move_to_player)
        chase_node = SequenceNode('Chase')
        chase_node.add_children(find_player_node, move_to_player_node)


        chase_wander_node = SelectorNode('Chase or Wander')
        chase_wander_node.add_children(chase_node, wander_node)



        self.bt = BehaviorTree(chase_wander_node)
        # fill here
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        dist = (server.player.x - self.x)**2 + (server.player.y - self.y)**2
        # if dist < 100**2:
        #     self.x = (1 - 0.8) * self.x + 0.8 * m.player.x  # 0.1
        #     self.y = (1 - 0.8) * self.y + 0.8 * m.player.y

        if self.HP == 0:
            game_world.remove_object(self)

        if dist < 10**2:
            if server.player.cur_state == AttackState:
                self.HP -= 10
                print('monster1 HP=', self.HP)
                pass

    def draw(self):
        self.image.clip_draw(0, 32*3, 32, 32, self.x, self.y)