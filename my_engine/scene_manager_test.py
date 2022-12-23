from scene_manager import SceneManager
from scenes.title import TitleScene

def test_scene_manager():
    title_scene = TitleScene()
    scene_manager = SceneManager()
    scene_manager.change_scene(title_scene)