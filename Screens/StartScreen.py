from Screens.Screen import Screen
from Components.Button import Button
import pygame
import Constants

class StartScreen(Screen):
    StartButton : Button 
    Buttons : list[Button] = []
    def __init__(self) -> None:
        super().__init__()
        self.StartButton = Button(250,250,70,30,"Start",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.Buttons.append(self.StartButton)
        
        pass
    def handle_events(self, events )-> None:
        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.StartButton.is_hovered(pygame.mouse.get_pos()) :
                    print("switch to Game screen")
                    self.next_screen= "Game"
            pass
    
    def draw(self, screen)-> None:
        screen.fill(Constants.BACKGROUNDCOLOR)
        for Button in self.Buttons :
            Button.draw(screen)
       
    def update(self)-> None:
        mouse_pos = pygame.mouse.get_pos()
        for button in self.Buttons :
            button.update(mouse_pos)
        pass
    