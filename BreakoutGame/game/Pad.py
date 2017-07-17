from game.shared import *


class Pad(GameElement):

    def __init__(self, position, sprite):
        super(Pad, self).__init__(position, GameConstants.PAD_SIZE, sprite)

    def set_pos(self, position):
        new_position = [position[0], position[1]]
        size = self.get_size()

        if new_position[0] + size[0] > GameConstants.SCREEN_SIZE[0]:
            new_position[0] = GameConstants.SCREEN_SIZE[0] - size[0]

        # if new_position[0] + size[0] < GameConstants.SCREEN_SIZE[0]:
        #     new_position[0] = GameConstants.SCREEN_SIZE[0]

        super(Pad, self).set_pos(new_position)