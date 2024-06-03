from typing import Any
import pygame
import Constants

class Background(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("Data/gfx/Bg.jpg")
        self.image = pygame.transform.scale(self.image, (Constants.SCREEN_WIDTH, Constants.SCREEN_HIEGHT))
        self.rect =  pygame.Rect(0,0, Constants.SCREEN_WIDTH, Constants.SCREEN_HIEGHT)
        self.rect2 =  pygame.Rect(Constants.SCREEN_WIDTH-20,0, Constants.SCREEN_WIDTH, Constants.SCREEN_HIEGHT)

    def update(self) -> None:
        self.rect.x -= 5
        self.rect2.x = Constants.SCREEN_WIDTH + self.rect.x +10
        if self.rect.x < -Constants.SCREEN_WIDTH :
            self.rect.x = 0


        
     
    def draw(self,screen : pygame.surface.Surface) -> None :
        screen.blit(self.image,self.rect)
        screen.blit(self.image,self.rect2)
