import pygame
from load_image import load_image
from empire_lazer_bullet import empire_lazer_bullet

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class star_destroyer(pygame.sprite.Sprite):
    image = load_image("star_destroyer.png", colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.screen = screen
        self.image = pygame.transform.scale(star_destroyer.image, (117, 300))
        self.rect = self.image.get_rect()
        self.rect.x = 341
        self.rect.y = 0
        self.health = 1500
        self.damage = 100

    def shoot(self, x_pli, y_pli, *group):
        self.bullet = empire_lazer_bullet(self.rect.centerx, self.rect.centery, x_pli, y_pli, group)
