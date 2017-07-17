class GameElement:

    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__sprite = sprite

    def set_pos(self, position):
        self.__position = position

    def get_pos(self):
        return self.__position

    def get_size(self):
        return self.__size

    def get_sprite(self):
        return self.__sprite

    def __intersects_x(self, other):
        other_position = other.get_pos()
        other_size = other.get_size()

        if self.__position[0] >= other_position[0] and self.__position[0] <= (other_position[0] + other_size[0]):
            return True

        if (self.__position[0] + self.__size[0]) >= other_position[0] and (self.__position[0] + self.__size[0]) <= (other_position[0] + other_size[0]):
            return True

        return False

    def __intersects_y(self, other):
        other_position = other.get_pos()
        other_size = other.get_size()

        if self.__position[1] >= other_position[1] and self.__position[1] <= (other_position[1] + other_size[1]):
            return True

        if (self.__position[1] + self.__size[1]) >= other_position[1] and (self.__position[1] + self.__size[1]) <= (other_position[1] + other_size[1]):
            return True

        return False

    def intersects(self, other):
        return self.__intersects_x(other) and self.__intersects_y(other)