import pygame
import random
import os
import Constants

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Data\gfx\comet_6372069.png")
        self.sprite_sheet = pygame.image.load("Data\gfx\Falling_Star.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft =(0,0)
        self.rect.x = random.randint(Constants.SCREEN_WIDTH*0.3,Constants.SCREEN_WIDTH*1)
        self.rect.y = random.randint(-100,1)
        self.frames = []
        self.num_frames = 9
        self.current_frame = 0
        #self.load_frames(self.sprite_sheet.get_width()/9,self.sprite_sheet.get_height())
        self.load_frames()

    def load_frames(self):
        for i in range(0, 10):
            frame = pygame.image.load(os.path.join(r'Data\gfx\Meteors', f'pixil-frame-{i}.png'))
            frame = pygame.transform.scale(frame, (self.rect.width+10, self.rect.height+14))
            self.frames.append(frame)

    def load_frames1(self, frame_width, frame_height):
        for i in range(self.num_frames):
            frame = self.sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            self.frames.append(frame)

    def update(self) -> None:
        self.rect.move_ip(-2,5)
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.image = self.frames[self.current_frame]
        if self.rect.y > Constants.SCREEN_HIEGHT :
            self.rect.x = random.randint(Constants.SCREEN_WIDTH*0.3,Constants.SCREEN_WIDTH*1)
            self.rect.y = random.randint(-100,1)
          