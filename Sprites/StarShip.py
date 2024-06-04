from typing import Any
import pygame
import os
import Constants
class StarShip(pygame.sprite.Sprite) : 
   
    def __init__(self) -> None:
        super().__init__()
        self.rect =  pygame.Rect(50, Constants.SCREEN_HIEGHT/2 -20, Constants.PLAYER_WIDTH, Constants.PLAYER_HIEGHT)
        self.current_frame = 0
        self.frames = []
        self.load_frames()   
        self.image =self.frames[self.current_frame]
        self.dx = 2
        self.dy =3
    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.x +=0.1
            self.rect.y -= self.dy
        elif keys[pygame.K_DOWN]:
            self.rect.x -=0.2
            self.rect.y += self.dy
        if keys[pygame.K_RIGHT]  :
            self.rect.x += self.dx    
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.dx
        else :
            self.rect.move_ip(-0.3,1.4)
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.image = self.frames[self.current_frame]


        pass
    def load_frames(self):
        for i in range(1, 8):
            frame = pygame.image.load(os.path.join(r'Data\gfx\StarShip', f'pixil-frame-{i}.png'))
            frame = pygame.transform.scale(frame, (self.rect.width, self.rect.height))
            self.frames.append(frame)

     
    def is_Collide(self) -> None:
        pass
    
