from abc import ABC, abstractmethod

import pygame
from my_engine import my_game
from my_engine.scenes.scene_base import Scene


class Entity(ABC):

    @abstractmethod
    def __init__(self, game: my_game.MyGame, parent_scene: Scene):
        pass
    
    @abstractmethod
    def on_enter(self):
        pass

    @abstractmethod
    def on_exit(self):
        pass

    @abstractmethod
    def update(self, delta_time: int):
        pass

    @abstractmethod
    def draw(self, back_buffer: pygame.Surface):
        pass
