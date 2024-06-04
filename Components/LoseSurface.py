import pygame
import Constants
from Components.Button import Button
from Components.TextArea import TextArea
import Game
class LoseSurface :
    score : TextArea
    pause : TextArea
    Texts : list[TextArea] = [] 
    Restart : Button
    Buttons : list[Button] = []
    def __init__(self) -> None:
        #super().__init__(size)
        self.rect = pygame.Rect(Constants.SCREEN_WIDTH/2-200,Constants.SCREEN_HIEGHT/2-200,400,400)
        self.current_color = (247, 208, 138)
      #  self.font = pygame.font.Font(None,20)

        self.Restart =  Button(self.rect.centerx-35,self.rect.y*2,70,30,"Start",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.score = TextArea(None,"Score {}".format(Game.SCORE),20,(self.rect.x*1.3,self.rect.y*1.4))
        self.pause = TextArea(None,"You Lost",20,(self.rect.centerx,self.rect.y*1.2))
        self.Texts.append(self.pause)
        self.Texts.append(self.score)
        self.Buttons.append(self.Restart)
        pass
    def update(self) -> None:
        mouse_pos = pygame.mouse.get_pos()
        for button in self.Buttons :
            button.update(mouse_pos)
        self.score.setText("Score {}".format(Game.SCORE))
        pass
    def draw(self,screen : pygame.surface.Surface) :
        pygame.draw.rect(screen,self.current_color,self.rect)
        for text in self.Texts :
            text.draw(screen)
        for button in self.Buttons :
            button.draw(screen)
       
     
    

    
