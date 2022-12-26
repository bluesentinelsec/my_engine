#!/usr/bin/env python3

import sys
import os

# gross hack to import from parent directories
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
import my_engine.game
import gameplay

def main():
    # instantiate the game engine
    game = my_engine.game.MyGame(320, 200, 60, True, "data.dat")
    
    # instantiate level - pass game engine to scene
    game_scene = gameplay.Scene(game)

    # pass starting scene to game engine
    game.set_starting_scene(game_scene)

    # run game until quit
    game.run()

if __name__ == "__main__":
    main()