#!/usr/bin/env python3

import my_engine.game as engine
import scene_title as title


def main():
    # instantiate the game engine
    game = engine.Game(width=320, height=200, fps_cap=60, fullscreen=True)

    # instantiate first level/scene and pass game engine to scene
    title_scene = title.Scene(game)

    # pass starting scene to game engine
    game.set_starting_scene(title_scene)

    # start music from main so it plays in all scenes
    music_data = game.media_manager.get_file("media/music/music.wav")
    game.music_manager.load_music_file(music_data)
    game.music_manager.set_volume(0.3)
    game.music_manager.play_music(-1) # -1 loops music

    # run game until quit
    game.run()


if __name__ == "__main__":
    main()
