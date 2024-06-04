import pygame
import Constants
from Components.Button import Button
from Components.TextArea import TextArea
class PauseSurface() :
    Texts : list[TextArea] = [] 
    pause : TextArea
    Restart : Button
    Buttons : list[Button] = []
    def __init__(self) -> None:
        #super().__init__(size)
        self.rect = pygame.Rect(Constants.SCREEN_WIDTH/2-200,Constants.SCREEN_HIEGHT/2-200,400,400)
      
        self.current_color = (247, 208, 138)
      #  self.font = pygame.font.Font(None,20)
        self.pause = TextArea(None,"Pause",40,self.rect.center)
        self.Texts.append(self.pause)
        self.Restart = Button(self.rect.centerx-35,self.rect.y*2,70,30,"restart",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.Buttons.append(self.Restart)

        pass
    def update(self) -> None:
        mouse_pos = pygame.mouse.get_pos()
        for button in self.Buttons :
            button.update(mouse_pos)
        pass
    def draw(self,screen : pygame.surface.Surface) :
        pygame.draw.rect(screen,self.current_color,self.rect)
        for text in self.Texts :
            text.draw(screen)
        for button in self.Buttons :
            button.draw(screen)
       
     
    

    
