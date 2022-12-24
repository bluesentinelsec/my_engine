from abc import ABC, abstractmethod


import pygame

class Scene(ABC):

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def on_enter(self):
        pass

    @abstractmethod
    def on_exit(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def queue_free(self, entity_i):
        pass
