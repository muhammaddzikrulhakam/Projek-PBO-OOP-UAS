import pygame
from Text import Text


class Score(Text):
    def __init__(self, font, size, coordinate):
        self.font = font
        self.size = size
        self.coordinate = coordinate
        self.font = pygame.font.Font(self.font, self.size)
        self.score_value = 0

    def show(self, screen):
        score = self.font.render(
            "Score " + str(self.score_value), True, (255, 255, 255))
        screen.blit(score, self.coordinate)
