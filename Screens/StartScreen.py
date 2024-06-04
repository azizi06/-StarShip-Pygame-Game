from Screens.Screen import Screen
from Components.Button import Button
import pygame
import Constants

class StartScreen(Screen):
    StartButton : Button 
    AboutButton : Button
    Buttons : list[Button] = []
    def __init__(self) -> None:
        super().__init__()
        self.StartButton = Button(Constants.SCREEN_WIDTH/2-35,Constants.SCREEN_HIEGHT/2-30,70,30,"Start",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.AboutButton = Button(Constants.SCREEN_WIDTH-80,Constants.SCREEN_HIEGHT-100,50,30,"About",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.Buttons.append(self.StartButton)
        self.Buttons.append(self.AboutButton)
        
        pass
    def handle_events(self, events )-> None:
        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.StartButton.is_hovered(pygame.mouse.get_pos()) :
                    print("switch to Game screen")
                    Screen.next_screen= "Game"
                if self.AboutButton.is_hovered(pygame.mouse.get_pos()) :
                    Screen.next_screen = "About"
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
    