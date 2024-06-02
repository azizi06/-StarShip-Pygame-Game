import pygame, sys
import pygame.examples
import pygame.examples.aacircle
import pygame.examples.aliens
import pygame.examples.chimp
import pygame.examples.mask
import pygame.examples.stars
from pygame.locals import *
import Constants
from Components.Button import Button
from Screens.StartScreen import StartScreen
from Screens.GameScreen import GameScreen
import main1
class App:
    ScreenMap = {
            "Start" : StartScreen,
            "Game" : GameScreen
    }
    def __init__(self) -> None:
        self.runing = True
    def run(self):
        FPS =  pygame.time.Clock()
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HIEGHT))
        pygame.display.set_caption('StarShip Journey')
        currentScreen = StartScreen()
        while self.runing: # main game loop
            events = pygame.event.get()
        
            for event in events:
                if event.type == QUIT: 
                    pygame.quit()
                    sys.exit()
            currentScreen.draw(DISPLAYSURF)        
            currentScreen.handle_events(events=events)
            currentScreen.update()
            if currentScreen.next_screen :
                currentScreen = self.ScreenMap[currentScreen.next_screen]()
            
            pygame.display.update()     
            FPS.tick(Constants.FPS)
if __name__ == "__main__" :  
   App().run()