import pygame
import math
from pygame import mixer
from Entity import Entity


class Bullet(Entity):
    def __init__(self, bulletImg, bulletSound, coordinate):
        self.bulletX = coordinate[0]
        self.bulletY = coordinate[1]
        self.bulletX_change = 0
        self.bulletY_change = 10
        self.bullet_state = 'ready'

        self.bulletImg = pygame.image.load(bulletImg)
        self.bullet_sound = mixer.Sound(bulletSound)

    def draw(self, screen, x, y):
        self.bullet_state = 'fire'
        screen.blit(self.bulletImg, (x + 16, y + 10))

    def move(self, screen):
        if self.bulletY <= 0:
            self.bulletY = 480
            self.bullet_state = 'ready'

        if self.bullet_state == 'fire':
            self.draw(screen, self.bulletX, self.bulletY)
            self.bulletY -= self.bulletY_change

    def is_collision(self, enemy):
        distance = math.sqrt(math.pow(enemy.enemyX - self.bulletX, 2) +
                             math.pow(enemy.enemyY - self.bulletY, 2))
        if distance < 27:
            return True
        else:
            return False
