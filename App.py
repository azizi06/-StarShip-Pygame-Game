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
from Screens.AboutScreen import AboutScreen
from Screens.Screen import Screen

import main1
class App:
   
    def __init__(self) -> None:
        self.runing = True
        pygame.init()
        self.ScreenMap : dict[str,Screen] =  { 
            "About" : AboutScreen(),
            "Start" : StartScreen(),
            "Game" : GameScreen()
        }
      
       
    def run(self):
        FPS =  pygame.time.Clock()
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
            if Screen.next_screen :

                currentScreen = self.ScreenMap[Screen.next_screen]
                Screen.next_screen = None
            
            pygame.display.update()     
            FPS.tick(Constants.FPS)
if __name__ == "__main__" :
   App().run()