import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self,offset) -> None:
        super().__init__()
        self.image =pygame.image.load(r"Data\gfx\love_9783945.png")
        self.rect =self.image.get_rect()
        self.rect.x = 20+offset
        self.rect.y =20