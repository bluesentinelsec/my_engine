import argparse
import logging

import my_engine.game
import my_engine.scene_manager
import my_engine.scene
import my_engine.entity


def main(args):
    # setup console logging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')
    
    # setup the game engine
    g = my_engine.game.MyGame(320, 200, 60, args.fullscreen, args.media_file)
    s = my_engine.scene.Scene()
    g.set_starting_scene(s)

    m = my_engine.scene_manager.SceneManager()
    my_engine.entity.Entity(game=g, parent_scene=s, scene_manager=m)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("media_file", type=str)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-f", "--fullscreen", action="store_true")
    parser.add_argument("--fps", action="store_true")
    args = parser.parse_args()
    main(args)
    
