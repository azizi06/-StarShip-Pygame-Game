from typing import Any
import pygame
import os
import Constants
class StarShip(pygame.sprite.Sprite) : 
    width = Constants.PLAYER_WIDTH
    hieght = Constants.PLAYER_HIEGHT
    def __init__(self) -> None:
        super().__init__()
        self.current_frame = 0
        self.frames = []
        self.load_frames()   
        self.image =self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.y = Constants.SCREEN_HIEGHT/2-20
        self.rect.x = 50  
        
     
        
        
        pass
    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 3
        else :
            self.rect.move_ip(2,3)
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.image = self.frames[self.current_frame]


        pass
    def load_frames(self):
        for i in range(1, 8):
            frame = pygame.image.load(os.path.join(r'Data\gfx\StarShip', f'pixil-frame-{i}.png'))
            #frame = pygame.transform.scale(frame, (self.rect.width, self.rect.height))
            self.frames.append(frame)

     
    def is_Collide(self) -> None:
        pass
    
