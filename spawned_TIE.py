import pygame
import random
from load_image import load_image
from empire_lazer_bullet import empire_lazer_bullet

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class spawned_TIE(pygame.sprite.Sprite):
    image = load_image("TIE_fighter.png", colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.screen = screen
        self.image = pygame.transform.scale(spawned_TIE.image, (91, 80))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


    def shoot(self, x_pli, y_pli, *group):
        self.bullet = empire_lazer_bullet(self.rect.centerx, self.rect.centery, x_pli, y_pli, group)