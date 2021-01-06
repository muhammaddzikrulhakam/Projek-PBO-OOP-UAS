import random
import pygame
from pygame import mixer
from Entity import Entity

class Enemy(Entity):
    def __init__(self, enemyImg, explosion_sound):
        self.enemyX = None
        self.enemyY = None
        self.enemyX_change = 4
        self.enemyY_change = 40

        self.explosion_sound = mixer.Sound(explosion_sound)
        self.enemyImg = pygame.image.load(enemyImg)

    def draw(self, screen):
        screen.blit(self.enemyImg, (self.enemyX, self.enemyY))

    def move(self):
        self.enemyX += self.enemyX_change
        if self.enemyX <= 0:
            self.enemyX_change = 4
            self.enemyY += self.enemyY_change
        elif self.enemyX >= 736:
            self.enemyX_change = -4
            self.enemyY += self.enemyY_change

    def set_location(self, x, y):
        self.enemyX = random.randint(x[0], x[1])
        self.enemyY = random.randint(y[0], y[1])

    def death(self, bullet, score, collision):
        if collision:
            self.explosion_sound.play()
            bullet.bulletY = 480
            bullet.bullet_state = 'ready'
            score.score_value += 1
            self.set_location((0, 735), (50, 150))

    def is_enemy_win(self):
        if self.enemyY > 440:
            return True

    def gone(self):
        self.enemyY = float('inf')