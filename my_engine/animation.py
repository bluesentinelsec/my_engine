import my_engine.game
import my_engine.entity

import pygame


class Animator:
    def __init__(self, game: my_engine.game.MyGame) -> None:
        self.game = game
        self.frame_width = 0
        self.frame_height = 0
        self.total_frames = 0
        self.frame_time = 0
        self.current_frame = 0
        self.frame_image: pygame.Surface = None
        self.sprite_sheet: pygame.Surface = None
        self.is_animation_playing: bool = False
        self.skip_animation = False

    def init_animation(self, sprite_sheet: pygame.Surface, frame_width, frame_height, total_frames):
        self.sprite_sheet = sprite_sheet
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.total_frames = total_frames
        self.frame_image = self.sprite_sheet.subsurface(
            self.current_frame, 0, self.frame_width, self.frame_height)

    def play_animation(self, frame_duration=1000, loop=True):

        # skip animation if we're not looping
        if self.skip_animation:
            return

        # set animation state to true
        self.is_animation_playing = True

        # measure elapsed frame time
        self.frame_time += self.game.get_delta_time()

        # advance frame if frame time exceeds duration
        if self.frame_time >= frame_duration:

            # reset time on this frame
            self.frame_time = 0

            # advance to next frame
            self.current_frame += self.frame_width

            # if we reached final frame
            if self.current_frame >= self.frame_width * self.total_frames:

                # go to first frame
                self.current_frame = 0
                if not loop:
                    self.stop_animation()

            # extract frame from sprite sheet
            self.frame_image = self.sprite_sheet.subsurface(pygame.Rect(
                self.current_frame, 0, self.frame_width, self.frame_height))

    def stop_animation(self):
        self.is_animation_playing = False
        self.skip_animation = True

    def draw_animation(self, dst_rect: pygame.Rect):
        self.game.screen.blit(self.frame_image, dst_rect)
