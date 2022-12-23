from my_engine.scenes import title
from my_engine import my_game

def test_title():
    game = my_game.MyGame()
    game.easy_init(320, 200, False)

    title_scene = title.TitleScene(game=game)
    title_scene.on_enter()
    title_scene.update()
    title_scene.draw()
    title_scene.on_exit()

    game.quit_game()