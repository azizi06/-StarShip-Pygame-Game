
from Screens.Screen import Screen
import pygame
from Components.Button import  Button
class GameScreen(Screen) :
    GameScreenGroup : pygame.sprite.Group
    HomeButton : Button
    Buttons : list[Button] =[]
    
    def __init__(self) -> None:
        super().__init__()
        self.HomeButton =  Button(20,20,70,30,"Home",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.Buttons.append(self.HomeButton)
        pass
    def update(self)-> None:
        mouse_pos = pygame.mouse.get_pos()
        for button in self.Buttons :
            button.update(mouse_pos)
        pass
    def draw(self, screen)-> None:
        screen.fill((234,122,178))
        for button in self.Buttons :
            button.draw(screen)
        return super().draw(screen)
    def handle_events(self, events)-> None:
        mouse_pos = pygame.mouse.get_pos()
        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.HomeButton.is_hovered(mouse_pos):
                    self.next_screen = "Start"


         
      