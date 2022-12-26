import my_engine.game
import my_engine.scene
import my_engine.scene_manager

import pygame


class Entity():
    def __init__(self, game: "my_engine.game.MyGame", parent_scene: "my_engine.scene.Scene",
                 scene_manager: "my_engine.scene_manager.SceneManager") -> None:
        self.group = ""  # identifies the entity type to support collission detection
        self.is_active = True  # used to pause/unpause the entity
        self.image: pygame.Surface = None  # store the entity sprite image
        self.rect: pygame.Rect = None  # contains entity x/y position, width/height, etc.
        self.speed = 0  # how fast is the entity?
        self.angle = 0  # what angle does the entity face?
        self.scale = 0  # should we stretch/shrink the entity?
        self.game = game
        self.scene_manager = scene_manager
        self.parent_scene = parent_scene
        # ToDo: animation member variables

    def set_group(self, group):
        self.group = group

    def set_x_position(self, x_pos):
        self.rect.x = x_pos

    def set_y_position(self, y_pos):
        self.rect.y = y_pos

    def set_speed(self, speed):
        self.speed = speed

    def set_angle(self, angle):
        self.angle = angle

    def set_scale(self, scale):
        self.scale = scale

    def deactivate(self):
        self.is_active = False

    def set_image(self, image: pygame.Surface):
        # load image by file name from media manager
        self.image = image
        self.set_rect(self.image.get_rect())

    def set_rect(self, rect: pygame.Rect):
        self.rect = rect

    def set_screen_height(self, height):
        self.screen_height = height

    def set_screen_width(self, width):
        self.screen_width = width

    def check_collision(self, entity_to_check: "Entity") -> bool:
        return self.rect.colliderect(entity_to_check.rect)

    def on_load(self):
        pass

    def update(self, delta_time: int):
        pass

    def on_exit(self):
        pass
