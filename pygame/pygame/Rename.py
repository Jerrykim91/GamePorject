import pygame, sys
from pygame.locals import QUIT,KEYDOWN

class T:
    def __init__(self):
        pygame.init()
        #pygame.display.init()
        screen = pygame.display.set_mode((200, 200))
        #backgroundImg = pygame.image.load( './data/icon.png' )
        #print( backgroundImg.get_size() )
        Run = True
        while Run:
            pygame.time.Clock().tick(30)
            EVENTS = pygame.event.get()
            for event in EVENTS:
                if event.type == QUIT:
                    Run = False
            #screen.blit(backgroundImg, (0, 0))
            screen.fill(pygame.color.Color(255, 0, 0))
            pygame.display.flip()
            #pygame.display.update()

        pygame.display.quit()
        pygame.quit()
        sys.exit()

T()