import pygame
from spritesheet import Spritesheet;
class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        sprite = Spritesheet("Data\gfx\starship.png")
        self.vel=10
        self.index = 0
        self.images =[sprite.parse_sprite(0),sprite.parse_sprite(1),sprite.parse_sprite(2),sprite.parse_sprite(3),sprite.parse_sprite(4),sprite.parse_sprite(5)]
        self.image =self.images[self.index]
       
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y =100
        self.moving = False
      
    def update(self,keys,screen_size)  :
        if self.index==5 :
            self.index =1
        if keys[pygame.K_LEFT] and self.rect.x>5:
            self.rect.x= self.rect.x-self.vel 
            self.index+=1
        

        if (keys[pygame.K_UP] or keys[pygame.MOUSEBUTTONUP]  )and self.rect.y>30 :
           self.rect.y= self.rect.y-self.vel
           self.index+=1
           

        if keys[pygame.K_DOWN] and self.rect.y< screen_size[1]-140:
            self.rect.y= self.rect.y+self.vel
            self.index+=1
            

        if (keys[pygame.K_RIGHT] or keys[pygame.MOUSEBUTTONDOWN])and self.rect.x< screen_size[0]-4 :
           self.rect.x= self.rect.x +self.vel
           self.index+=1
    

        if not (keys[pygame.K_LEFT] and keys[pygame.K_UP] and keys[pygame.K_DOWN] and [pygame.K_RIGHT] and keys[pygame.MOUSEBUTTONUP] and keys[pygame.MOUSEBUTTONDOWN] )and  self.rect.y< screen_size[1]-45 and   self.rect.x< screen_size[0]-45 and self.rect.x >0 and self.rect.y >0 :
            self.index =0
            self.rect.y =self.rect.y +3.2
            self.index = 0
            
        

        
 