import pygame, sys
from pygame.locals import *
import Constants
from Components.Button import Button
from Screens.StartScreen import StartScreen
from Screens.GameScreen import GameScreen
import main1
def main():
    FPS =  pygame.time.Clock()
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HIEGHT))
    pygame.display.set_caption('StarShip Journey')
    currentScreen = StartScreen()
    ScreenMap = {
        "Start" : StartScreen,
        "Game" : GameScreen

    }
    while True: # main game loop
        events = pygame.event.get()
       
        for event in events:
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
        currentScreen.draw(DISPLAYSURF)        
        currentScreen.handle_events(events=events)
        currentScreen.update()
        if currentScreen.next_screen :
            currentScreen = ScreenMap[currentScreen.next_screen]()
        
        pygame.display.update()     
        FPS.tick(Constants.FPS)
if __name__ == "__main__" :
   
    main()