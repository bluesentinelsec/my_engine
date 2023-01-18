#!/usr/bin/env python3

import logging
import my_engine.scene_loader as sl
import my_engine.game as gm


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    # create a game world
    game = gm.Game(fullscreen=False)

    # create scene loader class
    scene_loader = sl.SceneLoader(game_ptr=game)
    scene_loader.load_level_file("test_level.xml")

    # launch game loop
    game.run()


if __name__ == "__main__":
    main()
