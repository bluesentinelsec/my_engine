import logging
import xml.etree.ElementTree as ET

import my_engine.game as game
import my_engine.entity as ent
import my_engine.scene as sc

# import components
import my_engine.component_transform as tr
import my_engine.component_sprite as spr

from typing import List


class SceneLoader:
    def __init__(self, game_ptr: "game.Game") -> None:

        # give ptr to game world
        self.game_ptr = game_ptr

        # create a blank scene
        self.scene = sc.Scene(game=self.game_ptr, name="testing")

        # create a list to store created entities
        self.entity_list: List["ent.Entity"] = []

        # ToDo - refactor this function out?
        self.game_ptr.set_starting_scene(self.scene)

    def load_level_file(self, file):

        tree = ET.parse(file)
        entities_root = tree.getroot()

        # get each entity
        for each_entity in entities_root:
            s = each_entity.attrib

            # create entity instance
            ent_instance = ent.Entity(
                ent_type=s['type'], game=self.game_ptr, parent_scene=self.scene)

            # for each component in entity
            for component in each_entity:

                # get component attributes
                s = component.attrib

                # instantiate concrete component based on its type
                if s["type"] == "transform":

                    transform_comp = tr.TransformComponent(ent_instance)
                    transform_comp.set_position_x(s['x_position'])
                    transform_comp.set_position_y(s['y_position'])
                    transform_comp.set_rotation_degrees(s['rotation_degrees'])
                    transform_comp.set_scale_x(s['scale_x'])
                    transform_comp.set_scale_y(s['scale_y'])
                    ent_instance.add_component(transform_comp)

                elif s["type"] == "sprite":

                    spr_comp = spr.SpriteComponent(
                        image_file=s['image_file'], owner=ent_instance)

                    ent_instance.add_component(spr_comp)

                else:
                    logging.debug(
                        f"found unknown component of type: {s['type']}")

                # add configured entity to a list
                self.entity_list.append(ent_instance)

            # append all entities to scene
            print("adding entity to scene")
            for each_ent in self.entity_list:
                self.scene.add_entity(each_ent)

        # load scene
        self.game_ptr.scene_manager.change_scene(self.scene)
