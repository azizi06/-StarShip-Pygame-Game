import pygame
from pygame import Surface
from pygame.event import Event
from Screens.Screen import Screen
from Components.Button import Button
from Components.TextArea import TextArea

import Constants
class AboutScreen(Screen) :
    HomeButton : Button
    LinkedIn : TextArea
    Twitter : TextArea
    Github : TextArea
    msg : TextArea
    Texts : list[TextArea] = []
    Buttons : list[Button] = []
    def __init__(self) -> None:
        super().__init__()
        self.HomeButton =  Button(20,20,70,30,"Home",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.LinkedIn = TextArea(None,"azizi mohammed",20,(Constants.SCREEN_WIDTH*0.3,Constants.SCREEN_HIEGHT*8/10))
        self.Twitter = TextArea(None,"@azizi mohammed",20,(Constants.SCREEN_WIDTH*0.5,Constants.SCREEN_HIEGHT*0.8))
        self.Github = TextArea(None,"@azizi mohammed",20,(Constants.SCREEN_WIDTH*0.7,Constants.SCREEN_HIEGHT*8/10))
        self.Texts.append(self.Github)
        self.Texts.append(self.Twitter)
        self.Texts.append(self.LinkedIn)
        self.Buttons.append(self.HomeButton)
      
    def update(self) -> None:
        mouse_pos = pygame.mouse.get_pos()
        for text in self.Texts :
            text.update()
        for button in self.Buttons :
            button.update(mouse_pos)
        
    def draw(self, screen: Surface) -> None:
        screen.fill(Constants.BACKGROUNDCOLOR)
        for text in self.Texts :
            text.draw(screen)
        for button in self.Buttons :
            button.draw(screen)
    
    def handle_events(self, events: list[Event]) -> None:
        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.LinkedIn.is_hovered(pygame.mouse.get_pos()):
                    print("LinkedIn")
                if self.Twitter.is_hovered(pygame.mouse.get_pos()):
                    print("Twitter")
                if self.Github.is_hovered(pygame.mouse.get_pos()):
                    print("Github")
                if self.HomeButton.is_hovered(pygame.mouse.get_pos()):
                    Screen.next_screen = "Start"
                pass
            
              
        return super().handle_events(events)
