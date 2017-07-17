import pygame

class Scene:
    def __init__(self, game):
        self.__game = game
        self.__texts = []

    def render(self):
        for text in self.__texts:
            self.__game.window.blit(text[0], text[1])

    def get_game(self):
        return self.__game

    def handle_events(self, events):
        pass

    def clear_text(self):
        self.__texts = []

    def add_text(self, string, x=0, y=0, colour=(255, 255, 255), background=(0, 0, 0), size=20):
        font = pygame.font.SysFont("Segoe UI", size)
        self.__texts.append([font.render(string, True, colour, background), (x, y)])