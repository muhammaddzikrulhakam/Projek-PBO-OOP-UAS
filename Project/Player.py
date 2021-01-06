import pygame
from Entity import Entity


class Player(Entity):
    def __init__(self, playerImg, coordinate):
        self.playerX = coordinate[0]
        self.playerY = coordinate[1]
        self.playerX_change = 0

        self.playerImg = pygame.image.load(playerImg)

    def draw(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.playerX_change = -5
        elif keys[pygame.K_RIGHT]:
            self.playerX_change = 5
        else:
            self.playerX_change = 0

        self.playerX += self.playerX_change

        # Pinggir Window
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 736:
            self.playerX = 736

    def shoot(self, keys, bullet, screen):
        if keys[pygame.K_SPACE]:
            if bullet.bullet_state == 'ready':
                bullet.bullet_sound.play()
                bullet.bulletX = self.playerX
                bullet.draw(screen, bullet.bulletX, bullet.bulletY)

    def is_exit_game(self, event):
        if event.type == pygame.QUIT:
            return False
        return True
