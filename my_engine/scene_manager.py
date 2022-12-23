from my_engine.scenes import scene_base
from typing import List

import pygame

class SceneManager:
    def __init__(self):
        self.scene_list: List[scene_base.Scene] = []

    def push_scene(self, scene_i: scene_base.Scene):
        self.scene_list.append(scene_i)
        self.scene_list[0].on_enter()

    def pop_scene(self):
        if len(self.scene_list) > 0:
            self.scene_list[0].on_exit()
            self.scene_list.pop()

    def change_scene(self, scene_i: scene_base.Scene):
        self.pop_scene()
        self.push_scene(scene_i)

    def update_scene(self):
        self.scene_list[0].update()

    def draw_scene(self):
        self.scene_list[0].draw()