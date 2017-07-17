from game.bricks import Brick
from game.shared import GameConstants

class LifeBrick(Brick):

    def __init__(self, position, sprite, game):
        super(LifeBrick, self).__init__(position, sprite, game)

    def hit(self):
        game = self.get_game()

        game.increase_lives()

        super(LifeBrick, self).hit()

    def get_hit_sound(self):
        return GameConstants.SOUND_LIFE