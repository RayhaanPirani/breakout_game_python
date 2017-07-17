import pygame
from game.scenes.Scene import Scene
from game.shared import *
from game import Highscore

class OverScene(Scene):

    def __init__(self, game):
        super(OverScene, self).__init__(game)
        self.__playername = ""
        self.__gameover_sprite = pygame.image.load(GameConstants.SPRITE_GAMEOVER)

    def render(self):
        self.get_game().window.blit(self.__gameover_sprite, (GameConstants.SCREEN_SIZE[0]/2 - GameConstants.SPRITE_GAMEOVER_SIZE[0]/2, GameConstants.SCREEN_SIZE[1] / 4))

        self.clear_text()
        self.add_text("Your name: ", 300, 400, size=36)
        self.add_text(self.__playername, 500, 400, size=36)
        super(OverScene, self).render()

    def handle_events(self, events):
        super(OverScene, self).handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = self.get_game()
                    Highscore().add(self.__playername, game.get_score())
                    game.reset()
                    # game.ftp_upload()
                    game.change_scene(GameConstants.SCORE_SCENE)
                elif event.key >= 65 and event.key <= 122:
                    self.__playername += chr(event.key)

                if event.key == pygame.K_F1:
                    self.get_game().reset()
                    self.get_game().change_scene(GameConstants.PLAYING_SCENE)

                if event.key == pygame.K_ESCAPE:
                    exit()