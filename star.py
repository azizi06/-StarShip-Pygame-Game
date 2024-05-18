import random
import pygame

class Star(pygame.sprite.Sprite):
    def __init__(self,screen_size):
        super().__init__()
        self.image = pygame.image.load(r"Data\gfx\star_2956792.png")
        self.rect = self.image.get_rect()
        self.rect.topleft =(0,0)
        self.rect.x = random.randint(screen_size[0]*0.8,screen_size[0]*0.9)
        self.rect.y = random.randint(screen_size[1]*0.30,screen_size[1]*0.8)
    def update(self) -> None:
        self.rect.move_ip(-6,0.2)