import my_engine.game as engine
import my_engine.scene as parent
import my_engine.transitions as transitions

from typing import List

# import needed entities
import gameplay_background
import player
import opponent
import ball
import score


class Scene(parent.Scene):
    def __init__(self, game: "engine.MyGame") -> None:
        super().__init__(game)

    def on_load(self):

        transitions.fade_in(self.game)

        # load entities and add to scene
        game_background = gameplay_background.Background(
            "background", self.game, parent_scene=self)
        self.add_entity(game_background)

        player_ent = player.Player("player", self.game, parent_scene=self)
        self.add_entity(player_ent)

        
        opponent_ent = opponent.Opponent(
            "opponent", self.game, parent_scene=self)
        self.add_entity(opponent_ent)
        

        ball_ent = ball.Ball("ball", self.game, parent_scene=self)
        self.add_entity(ball_ent)

        player_score = score.Score("player_score", self.game, parent_scene=self)
        player_score.set_x_position((self.game.screen_w / 2) - 64)
        self.add_entity(player_score)

        opponent_score = score.Score("opponent_score", self.game, parent_scene=self)
        opponent_score.set_x_position((self.game.screen_w / 2) + 32)
        self.add_entity(opponent_score)

        opponent_ent.set_ball_ptr(ball_ent)
        ball_ent.get_entity_pointers()

    def on_exit(self):
        transitions.fade_out(self.game)
