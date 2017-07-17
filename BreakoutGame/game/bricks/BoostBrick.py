from game.bricks import Brick
from game.shared import *


class BoostBrick(Brick):
    def __init__(self, position, sprite, game):
        super(BoostBrick, self).__init__(position, sprite, game)

    def hit(self):
        game = self.get_game()

        for ball in game.get_balls():
            ball.set_speed(ball.get_speed() + 1)

        super(BoostBrick, self).hit()

    def get_hit_sound(self):
        return GameConstants.SOUND_BOOST