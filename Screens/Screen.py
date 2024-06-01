import pygame
import Constants
class Screen:
    ScreenGroup : pygame.sprite.Group
    def __init__(self) -> None:
        self.next_screen = None

    def handle_events(self, events : list[pygame.event.Event]) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self, screen : pygame.surface.Surface)-> None :
       
        pass
