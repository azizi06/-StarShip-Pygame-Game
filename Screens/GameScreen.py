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
from Components.LoseSurface import LoseSurface
from Components.TextArea import TextArea
import Constants
import Game
class GameScreen(Screen) :
    PauseScreen = PauseSurface()
    LoseScreen = LoseSurface()
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
    lose : bool = False
    ScoreTextArea : TextArea
    Texts : list[TextArea] = []
    
    def __init__(self) -> None:
        super().__init__()
        self.HomeButton =  Button(20,20,70,30,"Home",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.PauseButton = Button(Constants.SCREEN_WIDTH*0.6,20,30,30,"Pause",pygame.font.Font(None,20),(99,34,213),(120,70,19))
        self.Buttons.append(self.HomeButton)
        self.Buttons.append(self.PauseButton)
        self.Player.add(self.player)
        self.Health.add(Heart(Constants.SCREEN_WIDTH-100))
        self.Health.add(Heart(Constants.SCREEN_WIDTH-150))
        self.Health.add(Heart(Constants.SCREEN_WIDTH-200))
        self.Health.add(Heart(Constants.SCREEN_WIDTH-250))
        self.Health.add(Heart(Constants.SCREEN_WIDTH-300))
        self.ScoreTextArea = TextArea(None,"Score {}".format(Game.SCORE),20,(Constants.SCREEN_WIDTH*0.4,20))
        self.Texts.append(self.ScoreTextArea)
        
      

        pass
    def update(self)-> None:
        
        mouse_pos = pygame.mouse.get_pos()
        for button in self.Buttons :
            button.update(mouse_pos)
        
        self.Background.update()
        if not self.pause and not self.lose :    
            self.player.update()
            self.Meteors.update()
            self.Health.update()
            self.Stars.update()
        elif self.pause :
            self.PauseScreen.update()
        elif self.lose :
           self.LoseScreen.update()
           """  for button in self.LoseScreen.Buttons :
                button.update(mouse_pos)
            for text in self.LoseScreen.Texts :
                text.update() """
          
    def draw(self, screen)-> None:
        self.Background.draw(screen)
        for button in self.Buttons :
            button.draw(screen)
        for text in self.Texts :
            text.draw(screen)
        self.Player.draw(screen)
        self.Meteors.draw(screen)
        self.Stars.draw(screen)
        self.Health.draw(screen)
        if self.pause :
            self.PauseScreen.draw(screen)
        if self.lose :
            self.LoseScreen.draw(screen)

    def handle_events(self, events)-> None:
        mouse_pos = pygame.mouse.get_pos()
        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.HomeButton.is_hovered(mouse_pos) :
                    print("switch to Start screen")
                    Screen.next_screen = "Start"
                if self.PauseButton.is_hovered(mouse_pos) and not self.lose:
                    self.pause = not self.pause
        if not self.lose :
            self.CeckCollide()
      
    def CeckCollide(self) -> None :
        MeteorsCollitionList : list[Meteor] = pygame.sprite.spritecollide(self.Player.sprites()[0],self.Meteors,dokill=True)
        StarsCollitionList : list[Meteor] = pygame.sprite.spritecollide(self.Player.sprites()[0],self.Stars,dokill=True)
        if pygame.sprite.Group.__len__(self.Meteors) == 0:
            rand : int = random.randint(Constants.METEOR_NUMBER,Constants.METEOR_NUMBER*2)
            for i in range(rand) :
                pass
                self.Meteors.add(Meteor())
        if pygame.sprite.Group.__len__(self.Stars) == 0:
            rand : int = random.randint(Constants.METEOR_NUMBER,Constants.METEOR_NUMBER*2)
            for i in range(rand) :
                self.Stars.add(Star())
        if len(StarsCollitionList) :
            Game.SCORE += len(StarsCollitionList)
            self.ScoreTextArea.setText("Score {}".format(Game.SCORE))
        if len(MeteorsCollitionList) :
            self.Health.sprites()[-1].kill() if pygame.sprite.Group.__len__(self.Health) != 0 else 0
            if pygame.sprite.Group.__len__(self.Health) == 0 :
                self.lose = True

                self.player.kill()
    def restart(self) -> None :
        pass
        

        
