import pygame
import sys
import random
import os
from load_image import load_image

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class asteroid(pygame.sprite.Sprite):
    image = load_image(random.choice(["asteroid_1.png", "asteroid_2.png"]), colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image_1 = pygame.transform.scale(asteroid.image, (40, 34))
        self.image = self.image_1.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(0, 34)
        self.speedy = random.randrange(1, 6)
        self.mask = pygame.mask.from_surface(self.image_1)
        self.speedx = random.randrange(-3, 3)
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > 600 + 10 or self.rect.left < -25 or self.rect.right > 800 + 20:
            self.kill()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            new_image = pygame.transform.rotate(self.image_1, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center