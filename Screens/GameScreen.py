import random
from Screens.Screen import Screen
import pygame
from Components.Button import  Button
from Sprites.StarShip import StarShip
from Sprites.Health import Heart
from Sprites.meteor import Meteor
from Sprites.Star import Star
from Components.Background import Background
from Components.PauseSurface import PauseSurface
import Constants
class GameScreen(Screen) :
    PauseScreen = PauseSurface()
    Meteors : pygame.sprite.Group = pygame.sprite.Group()
    Stars : pygame.sprite.Group = pygame.sprite.Group()
    Player : pygame.sprite.Group = pygame.sprite.GroupSingle()
    Health : pygame.sprite.Group = pygame.sprite.Group()
    Background : pygame.sprite.Sprite = Background()
    HomeButton : Button
    PauseButton : Button
    Buttons : list[Button] =[]
    player : pygame.sprite.Sprite = StarShip()
    pause : bool = False
    
    def __init__(self) -> None:
        super().__init__()
        self.HomeButton =  Button(20,20,70,30,"Home",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.PauseButton = Button(Constants.SCREEN_WIDTH/2,20,30,30,"Pause",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.Buttons.append(self.HomeButton)
        self.Buttons.append(self.PauseButton)
        self.Player.add(self.player)
        self.Health.add(Heart(Constants.SCREEN_WIDTH-100))
        self.Health.add(Heart(Constants.SCREEN_WIDTH-150))
        self.Health.add(Heart(Constants.SCREEN_WIDTH-200))
        self.Health.add(Heart(Constants.SCREEN_WIDTH-250))
        self.Health.add(Heart(Constants.SCREEN_WIDTH-300))
        
      

        pass
    def update(self)-> None:
        
        mouse_pos = pygame.mouse.get_pos()
        for button in self.Buttons :
            button.update(mouse_pos)
        self.Background.update()
        if not self.pause :    
            self.player.update()
            self.Meteors.update()
            self.Health.update()
            self.Stars.update()
        else :
            self.PauseScreen.update()
        
        pass
    def draw(self, screen)-> None:
        self.Background.draw(screen)
        for button in self.Buttons :
            button.draw(screen)
        self.Player.draw(screen)
        self.Meteors.draw(screen)
        self.Stars.draw(screen)
        self.Health.draw(screen)
        if self.pause :
            self.PauseScreen.draw(screen)

    def handle_events(self, events)-> None:
        mouse_pos = pygame.mouse.get_pos()
        MeteorsCollitionList : list[Meteor] = pygame.sprite.spritecollide(self.Player.sprites()[0],self.Meteors,dokill=True)
        StarssCollitionList : list[Meteor] = pygame.sprite.spritecollide(self.Player.sprites()[0],self.Stars,dokill=True)
        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.HomeButton.is_hovered(mouse_pos):
                    print("switch to Start screen")
                    self.next_screen = "Start"
                if self.PauseButton.is_hovered(mouse_pos):
                    self.pause = not self.pause
        if pygame.sprite.Group.__len__(self.Meteors) == 0:
            rand : int = random.randint(Constants.METEOR_NUMBER,Constants.METEOR_NUMBER*2)
            for i in range(rand) :
                pass
                self.Meteors.add(Meteor())
        if pygame.sprite.Group.__len__(self.Stars) == 0:
            rand : int = random.randint(Constants.METEOR_NUMBER,Constants.METEOR_NUMBER*2)
            for i in range(rand) :
                self.Stars.add(Star())
        if len(MeteorsCollitionList) :
            self.Health.sprites()[-1].kill() if pygame.sprite.Group.__len__(self.Health) != 0 else 0
            if pygame.sprite.Group.__len__(self.Health) == 0 :
                pass
              #  self.player.kill()
        
        
