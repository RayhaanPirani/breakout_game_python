import os, fileinput, pygame, random
from game.bricks import *
from game.shared import GameConstants


class Level:
    def __init__(self, game):
        self.__game = game
        self.__bricks = []
        self.__brick_count = 0
        self.__current_level = GameConstants.DEFAULT_LEVEL

    def get_bricks(self):
        return self.__bricks

    def get_brick_count(self):
        return self.__brick_count

    def brick_hit(self):
        self.__brick_count -= 1

    def load_next_level(self):
        self.__current_level += 1
        file = os.path.join("assets", "leveldata", "level" + str(self.__current_level) + ".dat")

        if not os.path.exists(file):
            self.load_random()
        else:
            self.load(self.__current_level)

    def load(self, level):
        self.__current_level = level
        self.__bricks = []
        self.__brick_count = 0
        try:
            pad_pos = self.__game.get_pad().get_pos()
            for ball in self.__game.get_balls(): ball.set_pos((pad_pos[0] / 2, pad_pos[1] - GameConstants.PAD_SIZE[1]))
        except:
            pass

        x, y = 0, 0

        # level_file = open(os.path.join("assets", "leveldata", "level" + str(level) + ".dat"))
        # level_data = level_file.read()
        for line in fileinput.input(os.path.join("assets", "leveldata", "level" + str(level) + ".dat")):
            # for line in level_data.splitlines():
            for curr_brick in line:
                if curr_brick == '1':
                    brick_sprite = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick_sprite)
                    self.__brick_count += 1
                elif curr_brick == '2':
                    brick_sprite = BoostBrick([x, y], pygame.image.load(GameConstants.SPRITE_BOOSTBRICK), self.__game)
                    self.__bricks.append(brick_sprite)
                    self.__brick_count += 1
                elif curr_brick == '3':
                    brick_sprite = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick_sprite)
                    self.__brick_count += 1
                x += GameConstants.BRICK_SIZE[0]
            x = 0
            y += GameConstants.BRICK_SIZE[1]

    def load_random(self):
        self.__bricks = []
        self.__brick_count = 0
        try:
            pad_pos = self.__game.get_pad().get_pos()
            for ball in self.__game.get_balls(): ball.set_pos((pad_pos[0] / 2, pad_pos[1] - GameConstants.PAD_SIZE[1]))
        except:
            pass

        x, y = 0, 0

        max_bricks = int(GameConstants.SCREEN_SIZE[0] / GameConstants.BRICK_SIZE[0])
        rows = random.randint(2, 8)
        super_bricks = 0

        for row in range(0, rows):
            for brick in range(0, max_bricks):
                brick_type = random.randint(0, 3)
                if brick_type == 1 or super_bricks >= 3:
                    brick_sprite = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick_sprite)
                    self.__brick_count += 1
                elif brick_type == 2:
                    brick_sprite = BoostBrick([x, y], pygame.image.load(GameConstants.SPRITE_BOOSTBRICK),
                                              self.__game)
                    self.__bricks.append(brick_sprite)
                    self.__brick_count += 1
                    super_bricks += 1
                elif brick_type == 3:
                    brick_sprite = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick_sprite)
                    self.__brick_count += 1
                    super_bricks += 1

                x += GameConstants.BRICK_SIZE[0]
            x = 0
            y += GameConstants.BRICK_SIZE[1]
