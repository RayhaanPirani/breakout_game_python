import pygame
from game.scenes.Scene import Scene
from game import Highscore
from game.shared import GameConstants

class ScoreScene(Scene):

    def __init__(self, game):
        super(ScoreScene, self).__init__(game)
        self.__highscore_sprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)

    def render(self):
        self.get_game().window.blit(self.__highscore_sprite, (GameConstants.SCREEN_SIZE[0]/2 - GameConstants.SPRITE_HIGHSCORE_SIZE[0]/2, 20))
        self.clear_text()
        highscore = Highscore()

        x, y = 350, 180
        for score in highscore.get_scores():
            self.add_text(score[0], x, y, size=28)
            self.add_text(str(score[1]), x + 200, y, size=28)
            y += 40

        self.add_text("Press F1 to start the game.", x - 50, y + 50, size=30)
        self.add_text("Press Esc to close the game.", x - 50, y + 100, size=30)

        super(ScoreScene, self).render()

    def handle_events(self, events):
        super(ScoreScene, self).handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.get_game().reset()
                    self.get_game().change_scene(GameConstants.PLAYING_SCENE)

                if event.key == pygame.K_ESCAPE:
                    exit()