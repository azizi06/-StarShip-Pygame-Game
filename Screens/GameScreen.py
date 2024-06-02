
from Screens.Screen import Screen
import pygame
from Components.Button import  Button
from Sprites.StarShip import StarShip
class GameScreen(Screen) :
    Meteors : pygame.sprite.Group = pygame.sprite.Group()
    Stars : pygame.sprite.Group = pygame.sprite.Group()
    Player : pygame.sprite.Group = pygame.sprite.GroupSingle()

    HomeButton : Button
    Buttons : list[Button] =[]
    player : pygame.sprite.Sprite = StarShip()
    
    def __init__(self) -> None:
        super().__init__()
        self.HomeButton =  Button(20,20,70,30,"Home",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.Buttons.append(self.HomeButton)
        self.Player.add(self.player)

        pass
    def update(self)-> None:
        mouse_pos = pygame.mouse.get_pos()
        for button in self.Buttons :
            button.update(mouse_pos)
        self.player.update()
        pass
    def draw(self, screen)-> None:
        screen.fill((234,122,178))
        for button in self.Buttons :
            button.draw(screen)
        self.Player.draw(screen)
        self.Meteors.draw(screen)
        self.Stars.draw(screen)

    def handle_events(self, events)-> None:
        mouse_pos = pygame.mouse.get_pos()
        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.HomeButton.is_hovered(mouse_pos):
                    print("switch to Start screen")
                    self.next_screen = "Start"
                if event.type == pygame.K_AC_BACK :
                    pass


         
      