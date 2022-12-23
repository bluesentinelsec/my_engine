from my_engine.scenes import scene_base
from my_engine import my_game

import logging

import pygame

class TitleScene(scene_base.Scene):

    def __init__(self, game: my_game.MyGame):
        logging.debug("TitleScene.__init__")
        self.game = game
    

    def on_enter(self):
        logging.debug("TitleScene.on_enter")


    def on_exit(self):
        logging.debug("TitleScene.on_exit")


    def update(self):
        logging.debug("TitleScene.update")
        logging.debug(self.game.delta_time)


    def draw(self):
        logging.debug("TitleScene.draw")
        logging.debug(self.game.back_buffer)