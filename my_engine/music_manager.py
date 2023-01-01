import pygame

class MusicManager:
    def __init__(self) -> None:
        self.volume = 0.7

    def load_music_file(self, file: str):
        pygame.mixer.music.load(file)

    def set_volume(self, volume: float):
        pygame.mixer.music.set_volume(volume)
    
    def play_music(self, loop=0):
        """
        pass -1 to loop music
        """
        pygame.mixer.music.play(loop)

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()