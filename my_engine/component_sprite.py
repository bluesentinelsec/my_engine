"""
note for self:
- this component needs to be reworked;
- the rect x/y positions aren't inheriting
- the transform component values (>_>)

perhaps we can just iterate over the owner's componenet list,
find the transform component, then get/set the values we want
"""

import my_engine.entity as ent
import my_engine.component_transform as tr
import my_engine.media as media

import pygame as pg


class SpriteComponent(tr.TransformComponent):
    def __init__(self, image_file: str, owner: "ent.Entity") -> None:
        self.component_type: str = "sprite"
        super().__init__(owner=owner, component_type=self.component_type)

        # get ptr to media manager singleton
        self.media_manager = media.MediaSingleton()

        # load image
        self.image: pg.Surface = None
        self.rect: pg.Rect = None

        self.set_image(image_file)  # automatically sets the rect

    def set_image(self, image_file):
        # load image by file name from media manager
        self.image = pg.image.load(
            self.media_manager.get_file(image_file))
        # self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    # setters
    def set_position_x(self, x_pos: float):
        self.position_x = x_pos
        self.rect.x = self.position_x

    def set_position_y(self, y_pos: float):
        self.position_y = y_pos
        self.rect.y = self.position_y

    def set_rotation_degrees(self, rot: float):
        self.rotation_degrees = rot
        self.image = pg.transform.rotate(self.rotation_degrees)

    def set_scale_x(self, x_scale: float):
        self.scale_x = x_scale
        self.image = pg.transform.scale(
            self.image, (self.scale_x, self.scale_y))

    def set_scale_y(self, y_scale: float):
        self.scale_y = y_scale
        self.image = pg.transform.scale(
            self.image, (self.scale_x, self.scale_y))

    def get_rect(self):
        return self.rect

    def draw(self):
        if not self.is_enabled:
            return
        self.owner.game.screen.blit(self.image, self.rect)

    def check_collision_rect(self, rect_to_check: pg.Rect) -> bool:
        return self.rect.colliderect(rect_to_check)
