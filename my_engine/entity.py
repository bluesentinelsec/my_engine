import uuid

import my_engine.game
import my_engine.scene
import my_engine.scene_manager

import pygame

from typing import List
from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, ent_type: str, game: "my_engine.game.MyGame", parent_scene: "my_engine.scene.Scene") -> None:
        self.id = uuid.uuid4() # uniquely identifies each entity
        self.entity_type: str = ent_type # identifies the entity type
        self.groups = List[str] # identifies groups the entity is a part of
        self.is_active = True  # used to pause/unpause the entity
        self.image: pygame.Surface = None  # store the entity sprite image
        self.rect: pygame.Rect = None  # contains entity x/y position, width/height, etc.
        self.speed = 0  # how fast is the entity?
        self.angle = 0  # what angle does the entity face?
        self.scale = 0  # should we stretch/shrink the entity?
        self.game = game
        self.parent_scene = parent_scene
        # ToDo: animation member variables

    def set_ent_type(self, ent_type: str):
        self.entity_type = ent_type

    def get_ent_type(self):
        return self.entity_type
    
    def set_groups(self, group: str):
        self.groups.append(group)

    def get_groups(self):
        return self.groups

    def set_x_position(self, x_pos):
        self.rect.x = x_pos

    def set_y_position(self, y_pos):
        self.rect.y = y_pos

    def get_x_position(self):
        return self.rect.x

    def get_y_position(self):
        return self.rect.y

    def set_speed(self, speed):
        self.speed = speed

    def set_angle(self, angle):
        self.angle = angle

    def set_scale(self, scale):
        self.scale = scale

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def set_image(self, image_file: str):
        # load image by file name from media manager
        self.image = pygame.image.load(self.game.media_manager.get_file(image_file))
        self.set_rect(self.image.get_rect())
        self.rect.x = 0
        self.rect.y = 0

    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect

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

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def on_exit(self):
        pass
