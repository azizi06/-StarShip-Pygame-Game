import pygame, sys
from pygame.locals import *
import Constants
from Button import Button
import main1
FPS =  pygame.time.Clock()
pygame.init()
DISPLAYSURF = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HIEGHT))

pygame.display.set_caption('StarShip Journey')
Circle = pygame.draw.circle(DISPLAYSURF,(255,0,0),(200,200),30,20)
Home = True

StartButton = Button(200,200,60,60,"start", pygame.font.Font(None, 24),(200,40,104),(95,12,76))


while True: # main game loop
    DISPLAYSURF.fill(Constants.BACKGROUNDCOLOR)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if StartButton.is_hovered(event.pos) :
                main1.StartGame()
                print("Cliking Button")
   
    StartButton.draw(DISPLAYSURF)
    StartButton.update(mouse_pos=mouse_pos)
    pygame.display.update()
    
    FPS.tick(Constants.FPS)
   