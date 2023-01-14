#!/usr/bin/env python3

import logging
import my_engine.scene_loader as sl

import my_engine.game as gm
import my_engine.scene as sc
import my_engine.entity as ent
from my_engine.component_sprite import SpriteComponent

def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    # create scene loader class
    scene_loader = sl.SceneLoader()
    scene_loader.read_scene_file("test_level.xml")

    # create a game world
    game = gm.Game(fullscreen=False)

    # create a scene
    test_scene = sc.Scene(game=game, name="testing")

    # create a player entity
    player_ent = ent.Entity(ent_type="player", game=game, parent_scene=test_scene)

    # give player entity a sprite component
    player_ent.add_component(SpriteComponent(image_file="media/images/player.png", owner=player_ent))

    # add player to scene
    test_scene.add_entity(player_ent)

    # set starting scene
    game.set_starting_scene(test_scene)

    # launch game loop
    game.run()


if __name__ == "__main__":
    main()
