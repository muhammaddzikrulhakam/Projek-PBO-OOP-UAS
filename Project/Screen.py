import pygame


class Screen:
    def __init__(self, caption, bg, icon, window):
        self.caption = caption
        self.window = window

        self.background = pygame.image.load(bg)
        self.icon = pygame.image.load(icon)

    def make_window(self):
        return pygame.display.set_mode(self.window)

    def make_caption_icon(self):
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(self.icon)

    def show_screen(self, display):
        display.fill((0, 0, 0))
        display.blit(self.background, (0, 0))
