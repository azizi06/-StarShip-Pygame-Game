import pygame
class TextArea :
    def __init__(self,font,text : str ,size : int,center) -> None:
        pygame.font.init()
        self.font = pygame.font.Font(font,size)
        self.text = text
        self.center = center
        self.surface = self.font.render(self.text, True, (0,0,0))
        self.rect = self.surface.get_rect(center=self.center)
    def update(self) -> None :
        pass
    def setText(self,text) -> None :
        self.text = text
    def draw(self,screen) -> None :
        #text_surface = self.font.render(self.text, True, (0,0,0))
        self.surface = self.font.render(self.text, True, (0,0,0)) 
        screen.blit(self.surface, self.rect)
    
    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
        