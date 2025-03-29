import pygame
from load_image import load_image

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
e1 = load_image("Explosion1.png")
e2 = load_image("Explosion2.png")
e3 = load_image("Explosion3.png")
e4 = load_image("Explosion4.png")
e5 = load_image("Explosion5.png")
e6 = load_image("Explosion6.png")
explos = list()
explos.append(pygame.transform.scale(e1, (25, 25)))
explos.append(pygame.transform.scale(e2, (25, 25)))
explos.append(pygame.transform.scale(e3, (25, 25)))
explos.append(pygame.transform.scale(e4, (25, 25)))
explos.append(pygame.transform.scale(e5, (25, 25)))
explos.append(pygame.transform.scale(e6, (25, 25)))


class Explosion_part1(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = explos[0]
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part2(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = explos[1]
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part3(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = explos[2]
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part4(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = explos[3]
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part5(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = explos[4]
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part6(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = explos[5]
        self.rect = self.image.get_rect()
        self.rect.center = center

class Explosion_part1_TIE(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(explos[0], (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part2_TIE(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(explos[1], (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part3_TIE(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(explos[2], (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part4_TIE(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(explos[3], (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part5_TIE(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(explos[4], (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = center


class Explosion_part6_TIE(pygame.sprite.Sprite):
    def __init__(self, center, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(explos[5], (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = center