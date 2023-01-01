#!/usr/bin/env python3

import sys
import os

# gross hack to import from parent directories
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
import my_engine.game as engine
import scene_title as title


def main():
    # instantiate the game engine
    game = engine.MyGame(width=320, height=200, fps_cap=60, fullscreen=False)

    # instantiate first level/scene and pass game engine to scene
    title_scene = title.Scene(game)

    # pass starting scene to game engine
    game.set_starting_scene(title_scene)

    # run game until quit
    game.run()


if __name__ == "__main__":
    main()
