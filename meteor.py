import pygame
import random

class Meteor(pygame.sprite.Sprite):
    def __init__(self,screen_size):
        super().__init__()
        self.image = pygame.image.load(r"Data\gfx\comet_6372069.png")
        self.rect = self.image.get_rect()
        self.rect.topleft =(0,0)
        self.rect.x = random.randint(screen_size[0]*0.3,screen_size[0]*1)
        self.rect.y = random.randint(-100,1)
    def update(self) -> None:
        self.rect.move_ip(-2,5)