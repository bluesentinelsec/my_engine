import argparse
import logging

from my_engine.my_game import MyGame
from my_engine.scenes import title


def main(args):
    # setup console logging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    game = MyGame(args.media_file)
    game.easy_init(screen_width=320, screen_height=200, fullscreen=args.disable_fullscreen)

    title_scene = title.TitleScene(game=game)
    game.set_starting_scene(title_scene)

    game.run_game()

    game.quit_game()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("media_file", type=str)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-d", "--disable_fullscreen", action="store_false")
    args = parser.parse_args()
    main(args)
