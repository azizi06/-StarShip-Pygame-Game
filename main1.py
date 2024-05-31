# Example file showing a basic pygame "game loop"
import pygame
from Health import Heart
from Player import Player
from star import Star 
from meteor import Meteor
import pygame.locals
import random
# pygame setup
def StartGame():
    pygame.init()
    screen_size = [1000,600]
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption("space_ship")
    Background_image = pygame.image.load("Data/gfx/Bg.jpg")
    scaled_background = pygame.transform.smoothscale(Background_image, screen_size)

    Background_position =[0,0]
    screen.blit(scaled_background,Background_position)
    Background_2=scaled_background
    scroll_speed =1
    player =Player()
    stars_collected =0
    ground_scroll =0
    cnt =0

    Dead =False
    star_sound = pygame.mixer.Sound(r"Data\sfx\collectcoin-6075.mp3")


    Health = pygame.sprite.Group()
    meteors=pygame.sprite.Group()
    stars =pygame.sprite.Group()
    players = pygame.sprite.Group()
    player = Player()
    players.add(player)

    x=5
    offset =0  
    Health_count =4

    for i in range(x):
        Health.add(Heart(offset))
        offset =offset+40

    Health_list = Health.sprites()

    for i in range(x):
        star=Star(screen_size)

        star.rect.x = random.randint(screen_size[0]*0.8,screen_size[0]*0.9)
        star.rect.y = random.randint(50,screen_size[1])

        stars.add(star)
    x=2

    def Print_to_screen(string : str,win,pos):
        font = pygame.font.SysFont(None, 35)
        text = font.render(string, True, (227, 99, 55))
        win.blit(text,pos)




    while running:
        pygame.time.delay(5)
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
    #Background Stuff
        Background_position[0]-=scroll_speed
        ground_scroll+=scroll_speed
        screen.blit(scaled_background, Background_position)
        screen.blit(Background_2, (screen_size[0]-ground_scroll, 0))
        if screen_size[0] -ground_scroll==0 :
            Background_position[0] =screen_size[0]
        if Background_position[0] == 0:
            ground_scroll=0      

        
        keys = pygame.key.get_pressed()
    #adding elements player/stars .... to the screen
        players.update(keys,screen_size)
        players.draw(screen)
        
        stars.draw(screen)
        Health.draw(screen)
        stars.update()

        meteors.draw(screen)
        meteors.update()
        pygame.display.update()

    #remove star when collision
        if pygame.sprite.spritecollide(player,stars,dokill=True,collided=None) :
            stars_collected += 1
            star_sound.play()

    
        Print_to_screen(str(stars_collected),screen,(100,70))
        
        
        if pygame.sprite.spritecollide(player,meteors,dokill=False,collided=None) :
            pygame.sprite.Sprite.kill(Health_list[Health_count])
            Health_count-=1
            player.rect.y = 250
            player.rect.x=  200
            pygame.time.delay(100)
            if Health_count == -1 :
                pygame.sprite.Sprite.kill(player)
            



        #generate new stars
        if  pygame.sprite.Group.__len__(stars)< 3 :

            stars.add(Star(screen_size))
            stars.add(Star(screen_size))
            if cnt%2 ==0:
                stars.add(Star(screen_size))
                stars.add(Star(screen_size))
                stars.add(Star(screen_size))
            if cnt%10 == 0 :
                stars.add(Star(screen_size))
                stars.add(Star(screen_size))




        for star in stars :
            if star.rect.x <0 :
                pygame.sprite.Sprite.kill(star)

    #game progress
    
        if  pygame.sprite.Group.__len__(meteors) <3 :       
            meteors.add(Meteor(screen_size))
            if cnt % 2 != 0:
                meteors.add(Meteor(screen_size))
            if cnt % 7 ==0 :
                meteors.add(Meteor(screen_size))
                meteors.add(Meteor(screen_size))
            if cnt %21 ==0 :
                meteors.add(Meteor(screen_size))
                meteors.add(Meteor(screen_size))
                meteors.add(Meteor(screen_size))
                meteors.add(Meteor(screen_size))
        for meteor in meteors :
            if meteor.rect.y >  900 :
                pygame.sprite.Sprite.kill(meteor)
        
        # RENDER YOUR GAME HERE
        cnt =cnt + 1
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
