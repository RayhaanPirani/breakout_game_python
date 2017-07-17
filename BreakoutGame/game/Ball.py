import pygame
from game.shared import GameElement, GameConstants

class Ball(GameElement):

    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 3
        self.__increment = [2, 2]
        self.__direction = [1, 1]
        self.__moving = False

        super(Ball, self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def set_speed(self, speed):
        self.__speed = speed

    def reset_speed(self):
        self.set_speed(3)

    def get_speed(self):
        return self.__speed

    def is_moving(self):
        return self.__moving

    def set_motion(self, moving):
        self.__moving = moving
        self.reset_speed()

    def change_direction(self, element):
        position = self.get_pos()
        size = self.get_size()
        element_position = element.get_pos()
        element_size = element.get_size()

        if position[1] > element_position[1] and position[1] < element_position[1] + element_size[1] and \
            position[0] > element_position[0] and position[0] > element_position[0] + element_size[0]:
            # self.set_pos((position[0], element_position[1] + element_size[1]))
            self.__direction[0] *= -1
        elif position[1] + size[1] > element_position[1] and position[1] + size[1] < element_position[1] + element_size[1] and \
            position[0] > element_position[0] and position[0] > element_position[0] + element_size[0]:
            # self.set_pos((position[0], element_position[1] - element_size[1]))
            self.__direction[1] *= -1
        elif position[0] + size[0] > element_position[0] and position[0] + size[0] < element_position[0] + element_size[0] and \
            position[0] > element_position[0] and position[0] > element_position[0] + element_size[0]:
            # self.set_pos((position[0] - size[0], element_position[1]))
            self.__direction[0] *= -1
        else:
            # self.set_pos((element_position[0] + element_size[0], position[1]))
            # self.__direction[0] *= -1
            self.__direction[1] *= -1

    def update_pos(self):
        if not self.is_moving():
            pad_position = self.__game.get_pad().get_pos()
            self.set_pos((pad_position[0] + GameConstants.PAD_SIZE[0] / 2, GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1] - GameConstants.BALL_SIZE[1] - 1))
            return

        position = self.get_pos()
        size = self.get_size()

        new_position = [position[0] + (self.__increment[0] * self.__speed * self.__direction[0]),
                        position[1] + (self.__increment[1] * self.__speed * self.__direction[1])]

        if new_position[0] + size[0] >= GameConstants.SCREEN_SIZE[0]:
            self.__direction[0] *= -1
            new_position =  [GameConstants.SCREEN_SIZE[0] - size[0], new_position[1]]
            self.__game.play_sound(GameConstants.SOUND_WALL)

        if new_position[0] <= 0:
            self.__direction[0] *= -1
            new_position =  [0, new_position[1]]
            self.__game.play_sound(GameConstants.SOUND_WALL)

        if new_position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            self.__direction[1] *= -1
            new_position =  [new_position[0], GameConstants.SCREEN_SIZE[1] - size[1]]

        if new_position[1] <= 0:
            self.__direction[1] *= -1
            new_position =  [new_position[0], 0]
            self.__game.play_sound(GameConstants.SOUND_WALL)

        self.set_pos(new_position)

    def is_dead(self):
        position = self.get_pos()
        size = self.get_size()

        if position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]: return True
        return False