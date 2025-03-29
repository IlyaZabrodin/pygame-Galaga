import pygame
import sys
import random
import os

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class empire_lazer_bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, x_pli, y_pli, *group):
        super().__init__(*group)
        self.image = pygame.Surface((2, 10))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        if y_pli > y:
            self.speedy = 7
        elif y_pli < y:
            self.speedy = -7
        else:
            self.speedy = 0
        if y_pli - y == 0:
            if x_pli < x:
                self.speedx = -7
            elif x_pli > x:
                self.speedx = 7
            else:
                self.speedx = 7
        else:
            if y_pli < y:
                self.speedx = (x_pli - self.rect.centerx) / ((y - y_pli) / 10)
            else:
                self.speedx = (x_pli - self.rect.centerx) / ((y_pli - y) / 10)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom < 0 or self.rect.bottom > 800:
            self.kill()
