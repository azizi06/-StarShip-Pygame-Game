import random
import pygame
import Constants

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Data\gfx\star_2956792.png")
        self.rect = self.image.get_rect()
        self.rect.topleft =(0,0)
        self.rect.x = random.randint(Constants.SCREEN_WIDTH*0.8,Constants.SCREEN_WIDTH*0.9)
        self.rect.y = random.randint(Constants.SCREEN_HIEGHT*0.30,Constants.SCREEN_HIEGHT*0.8)
    def update(self) -> None:
        self.rect.move_ip(-6,0.2)
        if self.rect.y > Constants.SCREEN_HIEGHT  or self.rect.x < 0:
            self.rect.x = random.randint(Constants.SCREEN_WIDTH*0.8,Constants.SCREEN_WIDTH*0.9)
            self.rect.y = random.randint(Constants.SCREEN_HIEGHT*0.30,Constants.SCREEN_HIEGHT*0.8)

           
        