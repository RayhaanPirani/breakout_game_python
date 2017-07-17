import os

class GameConstants:

    # SCREEN_SIZE = [950, 768]
    SCREEN_SIZE = [950, 800]
    BRICK_SIZE = [95, 32]
    BALL_SIZE = [16, 16]
    PAD_SIZE = [114, 24]

    SPRITE_MENU_SIZE = [591, 102]
    SPRITE_HIGHSCORE_SIZE = [463, 166]
    SPRITE_GAMEOVER_SIZE = [309, 83]

    SPRITE_BALL = os.path.join("assets", "ball.png")
    SPRITE_PAD = os.path.join("assets", "pad.png")
    SPRITE_BRICK = os.path.join("assets", "brick.png")
    SPRITE_BOOSTBRICK = os.path.join("assets", "boost.png")
    SPRITE_LIFEBRICK = os.path.join("assets", "life.png")
    SPRITE_HIGHSCORE = os.path.join("assets", "highscore.png")
    SPRITE_MENU = os.path.join("assets", "mainmenu.png")
    SPRITE_GAMEOVER = os.path.join("assets", "gameover.png")

    SOUNDFILE_OVER = os.path.join("assets", "gameover.wav")
    SOUNDFILE_BRICK = os.path.join("assets", "brickhit.wav")
    SOUNDFILE_LIFE = os.path.join("assets", "life.wav")
    SOUNDFILE_BOOST = os.path.join("assets", "boost.wav")
    SOUNDFILE_WALL = os.path.join("assets", "wallbounce.wav")
    SOUNDFILE_PAD = os.path.join("assets", "padbounce.wav")

    SOUND_OVER = 0
    SOUND_BRICK = 1
    SOUND_LIFE = 2
    SOUND_BOOST = 3
    SOUND_WALL = 4
    SOUND_PAD = 5

    PLAYING_SCENE = 0
    OVER_SCENE = 1
    SCORE_SCENE = 2
    MENU_SCENE = 3

    DEFAULT_LIVES = 1
    DEFAULT_SCORE = 0
    DEFAULT_LEVEL = 1
    MAX_LEVELS = 10

    # Removed for privacy reasons
    FTP_HOST = ""
    FTP_USERNAME = ""
    FTP_PASSWORD = ""