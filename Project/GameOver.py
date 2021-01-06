import pygame
from Text import Text


class GameOver(Text):
    def __init__(self, font, size, coordinate):
        self.font = font
        self.size = size
        self.coordinate = coordinate
        self.font = pygame.font.Font(self.font, self.size)

    def show(self, screen):
        over = self.font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over, self.coordinate)
