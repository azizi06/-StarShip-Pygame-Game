import pygame
import random
import Constants

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Data\gfx\comet_6372069.png")
        self.rect = self.image.get_rect()
        self.rect.topleft =(0,0)
        self.rect.x = random.randint(Constants.SCREEN_WIDTH*0.3,Constants.SCREEN_WIDTH*1)
        self.rect.y = random.randint(-100,1)
    def update(self) -> None:
        self.rect.move_ip(-2,5)
        if self.rect.y > Constants.SCREEN_HIEGHT :
            self.rect.x = random.randint(Constants.SCREEN_WIDTH*0.3,Constants.SCREEN_WIDTH*1)
            self.rect.y = random.randint(-100,1)
          