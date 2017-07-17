import pygame
from game.scenes.Scene import Scene
from game.shared import *

class MenuScene(Scene):

    def __init__(self, game):
        super(MenuScene, self).__init__(game)

        self.add_text("F1 - Start", x=350, y=350, size=36)
        self.add_text("F2 - Show highscore", x=350, y=410, size=36)
        self.add_text("F3 - Exit", x=350, y=470, size=36)

        self.__menusprite = pygame.image.load(GameConstants.SPRITE_MENU)

    def render(self):
        self.get_game().window.blit(self.__menusprite, (GameConstants.SCREEN_SIZE[0]/2 - GameConstants.SPRITE_MENU_SIZE[0]/2, GameConstants.SCREEN_SIZE[1] / 4))
        super(MenuScene, self).render()

    def handle_events(self, events):
        super(MenuScene, self).handle_events(events)

        for event in events:
            if event.type == pygame.QUIT: exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.get_game().change_scene(GameConstants.PLAYING_SCENE)
                if event.key == pygame.K_F2:
                    self.get_game().change_scene(GameConstants.SCORE_SCENE)
                if event.key == pygame.K_F3:
                    exit()