from pygame import mixer


class Music:
    def __init__(self, bg_music):
        self.bg_music = bg_music

    def play_bg_music(self):
        mixer.music.load(self.bg_music)
        mixer.music.play(-1)
