import pygame
from game.scenes.Scene import Scene
from game.shared import *

class PlayingScene(Scene):

    def __init__(self, game):
        super(PlayingScene, self).__init__(game)

    def render(self):
        super(PlayingScene, self).render()

        game = self.get_game()
        level = game.get_level()

        pad = game.get_pad()
        balls = game.get_balls()

        if level.get_brick_count() <= 0:
            for ball in balls:
                ball.set_motion(False)
            level.load_next_level()

        if game.get_lives() <= 0:
            game.play_sound(GameConstants.SOUND_OVER)
            game.change_scene(GameConstants.OVER_SCENE)


        for ball in balls:
            for other_ball in balls:
                if ball != other_ball and ball.intersects(other_ball):
                    ball.change_direction(other_ball)

            for brick in game.get_level().get_bricks():
                if not brick.is_destroyed() and ball.intersects(brick):
                    game.play_sound(brick.get_hit_sound())
                    brick.hit()
                    level.brick_hit()
                    game.increase_score(brick.get_hit_points())
                    ball.change_direction(brick)
                    break

            if ball.intersects(pad):
                game.play_sound(GameConstants.SOUND_PAD)
                ball.change_direction(pad)

            ball.update_pos()

            if ball.is_dead():
                ball.set_motion(0)
                game.reduce_lives()

            game.window.blit(ball.get_sprite(), ball.get_pos())

        for brick in game.get_level().get_bricks():
            if not brick.is_destroyed():
                game.window.blit(brick.get_sprite(), brick.get_pos())

        pad.set_pos((pygame.mouse.get_pos()[0], pad.get_pos()[1]))
        game.window.blit(pad.get_sprite(), pad.get_pos())

        self.clear_text()
        self.add_text("Score: " + str(game.get_score()), x=0, y =GameConstants.SCREEN_SIZE[1]-80, size=30)
        self.add_text("Lives: " + str(game.get_lives()), x=0, y =GameConstants.SCREEN_SIZE[1]-40, size=30)


    def handle_events(self, events):
        super(PlayingScene, self).handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.get_game().get_balls():
                    ball.set_motion(True)