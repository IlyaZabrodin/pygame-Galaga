import pygame
import random
from load_image import load_image
from empire_lazer_bullet import empire_lazer_bullet

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class TIE_fighter(pygame.sprite.Sprite):
    image = load_image("TIE_fighter.png", colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.screen = screen
        self.image = pygame.transform.scale(TIE_fighter.image, (91, 80))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(20, 100)
        self.mask = pygame.mask.from_surface(self.image)
        self.speedy = random.randrange(1, 3)
        self.speedx = random.randrange(-3, 3)
        self.health = 200
        self.damage = 50

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > 600 + 10 or self.rect.left < -25 or self.rect.right > 800 + 20:
            self.kill()

    def shoot(self, x_pli, y_pli, *group):
        self.bullet = empire_lazer_bullet(self.rect.centerx, self.rect.centery, x_pli, y_pli, group)