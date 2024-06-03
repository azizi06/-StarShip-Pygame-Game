import pygame
class TextArea :
    def __init__(self,font,text : str ,size : int,center) -> None:
        pygame.font.init()
        self.font = pygame.font.Font(font,size)
        self.text = text
        self.center = center
    def update(self,text) -> None :
        self.text = text
    def draw(self,screen) -> None :
        text_surface = self.font.render(self.text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=self.center)
        screen.blit(text_surface, text_rect)
        