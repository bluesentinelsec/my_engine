import logging

import my_engine.game
import my_engine.scene_manager
import my_engine.scene
import my_engine.entity


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    g = my_engine.game.MyGame(320, 200, 60, False, "data.dat")
    s = my_engine.scene.Scene()
    g.set_starting_scene(s)

    m = my_engine.scene_manager.SceneManager()
    my_engine.entity.Entity(game=g, parent_scene=s, scene_manager=m)


if __name__ == "__main__":
    main()
