import pygame, ftplib
import tkinter
import tkinter.messagebox as msg

from game import *
from game.scenes import *
from game.shared import GameConstants

class Breakout:

    def __init__(self):
        self.__lives = GameConstants.DEFAULT_LIVES
        self.__score = GameConstants.DEFAULT_SCORE

        self.__level = Level(self)
        self.__level.load(GameConstants.DEFAULT_LEVEL)
        # self.__level.load_random()

        self.__pad = Pad((GameConstants.SCREEN_SIZE[0]/2, GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1]),
                         pygame.image.load(GameConstants.SPRITE_PAD))
        self.__balls = [Ball([200, 400], pygame.image.load(GameConstants.SPRITE_BALL), self)]

        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)
        # self.window = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.FULLSCREEN, 32)
        pygame.display.set_caption("Breakout")
        pygame.mouse.set_visible(False)

        self.__clock = pygame.time.Clock()

        self.__scenes = (
            PlayingScene(self),
            OverScene(self),
            ScoreScene(self),
            MenuScene(self)
        )
        self.__current_scene = 3

        self.__sounds = (
            pygame.mixer.Sound(GameConstants.SOUNDFILE_OVER),
            pygame.mixer.Sound(GameConstants.SOUNDFILE_BRICK),
            pygame.mixer.Sound(GameConstants.SOUNDFILE_LIFE),
            pygame.mixer.Sound(GameConstants.SOUNDFILE_BOOST),
            pygame.mixer.Sound(GameConstants.SOUNDFILE_WALL),
            pygame.mixer.Sound(GameConstants.SOUNDFILE_PAD)
        )

    def start(self):
        while True:
            self.__clock.tick(60)
            self.window.fill((0, 0, 0))

            current_scene = self.__scenes[self.__current_scene]
            current_scene.handle_events(pygame.event.get())
            current_scene.render()

            pygame.display.update()

    def change_scene(self, scene):
        self.__current_scene = scene

    def get_level(self):
        return self.__level

    def get_score(self):
        return self.__score

    def increase_score(self, score):
        self.__score += score

    def get_lives(self):
        return self.__lives

    def get_balls(self):
        return self.__balls

    def get_pad(self):
        return self.__pad

    def play_sound(self, soundclip):
        sound = self.__sounds[soundclip]

        sound.stop()
        sound.play()

    def increase_lives(self):
        self.__lives += 1

    def reduce_lives(self):
        self.__lives -= 1

    def reset(self):
        self.__lives = GameConstants.DEFAULT_LIVES
        self.__score = GameConstants.DEFAULT_SCORE
        self.__level.load(GameConstants.DEFAULT_LEVEL)

    def ftp_upload(self):
        host = GameConstants.FTP_HOST
        username = GameConstants.FTP_USERNAME
        password = GameConstants.FTP_PASSWORD

        try:
            ftp = ftplib.FTP(host, username, password)
            ftp.cwd("/public_html/breakout")

            score_file = open("highscore.dat", 'rb')
            ftp.storbinary('STOR highscore.dat', score_file)

            score_file.close()
            # ftp.quit()
        except:
            tkwindow = tkinter.Tk()
            tkwindow.wm_withdraw()
            msg.showinfo("Error", "Failed to upload highscores.")

Breakout().start()