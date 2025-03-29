import pygame
import sqlite3
import os
from load_image import load_image
from lazer_bullet import lazer_bullet

pygame.init()
con = sqlite3.connect("Records.db")
cur = con.cursor()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
img_dir = os.path.join(os.path.dirname(__file__), 'img')
snd_dir = os.path.join(os.path.dirname(__file__), 'snd')
shoot_sound = pygame.mixer.Sound(os.path.join('data', 'shot.mp3'))


class Millineum_falcon(pygame.sprite.Sprite):
    image = load_image("falcon.png", colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.screen = screen
        self.image = pygame.transform.scale(Millineum_falcon.image, (80, 112))
        My_sql_query = """SELECT Health, Damage from Records WHERE Name = ?"""
        result = cur.execute(My_sql_query, ("Gosha",))
        record = result.fetchall()
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 450
        self.health = record[0][0]
        self.damage = record[0][1]
        self.speedx = 0
        self.speedy = 0

    def update(self):
        if self.rect.x <= 0:
            self.speedx = 0
            self.rect.x = 1
        if self.rect.x >= 720:
            self.speedx = 0
            self.rect.x = 719
        if self.rect.y <= 0:
            self.speedy = 0
            self.rect.y = 1
        if self.rect.y >= 488:
            self.speedy = 0
            self.rect.y = 487
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def shoot(self, x_pli, y_pli, *group):
        self.bullet = lazer_bullet(self.rect.centerx, self.rect.top, x_pli, y_pli, group)
        shoot_sound.play()
