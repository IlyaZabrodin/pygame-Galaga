import pygame
from load_image import load_image

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class galaxy_generator(pygame.sprite.Sprite):
    image = load_image("galaxy.png", colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.screen = screen
        self.image = pygame.transform.scale(galaxy_generator.image, (800, 600))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0