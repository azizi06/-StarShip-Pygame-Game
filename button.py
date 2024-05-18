import pygame
from pygame.sprite import _Group
class Button(pygame.sprite.Sprite):
    def __init__(self,h,w,col,text) -> None:
        super().__init__()
        self.hight=h
        self.width=w
        
        
