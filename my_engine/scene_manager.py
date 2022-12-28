import my_engine.scene

from typing import List


class SceneManager:
    def __init__(self):
        self.scene_list: List["my_engine.scene.Scene"] = []

    def push_scene(self, scene_i: "my_engine.scene.Scene"):
        self.scene_list.append(scene_i)
        self.scene_list[0].on_load()

    def pop_scene(self):
        if len(self.scene_list) > 0:
            self.scene_list[0].on_exit()
            self.scene_list.pop()

    def change_scene(self, scene_i: "my_engine.scene.Scene"):
        self.pop_scene()
        self.push_scene(scene_i)

    def update_scene(self):
        self.scene_list[0].update()

    def draw_scene(self):
        self.scene_list[0].draw()
