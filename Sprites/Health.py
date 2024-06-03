from typing import Any
import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self,position) -> None:
        super().__init__()
        self.image =pygame.image.load(r"Data\gfx\love_9783945.png")
        self.rect =self.image.get_rect()
        self.rect.x = position
        self.rect.y =20
    def update(self, *args: Any, **kwargs: Any) -> None:
        pass