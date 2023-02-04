import pygame, os, sys
from pygame.locals import *


#start pygame
pygame.init()
#set fps refresh clock function
fpsClock = pygame.time.Clock()
#display screensize
surface = pygame.display.set_mode ((800,600))
pygame.display.set_caption("UniQuest")

#set background image of game
black = pygame.Color(0,0,0)
background = pygame.image.load('background.png').convert() #convert to correct image setting

#font for user input
base_font = pygame.font.Font(None,32)
user_text = ''

#Rectangle for user textbox
input_rect = pygame.Rect(500,500,200,50)

#Color of box when user selects it
color_active = pygame.Color('floralwhite')
#Color of box before user selects
color_passive = pygame.Color('floralwhite')

active = False

while True:
        surface.fill(black)
        for event in pygame.event.get(): #This is "while" the pygame file is open
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                        active = True
                else: 
                        active = False

            if event.type == pygame.KEYDOWN:
                if active:
                        if event.key == pg.K_RETURN:
                                print(user_text)
                                user_text=''
                        elif event.key == pygame.K_BACKSPACE:
                                user_text = user_text[:-1]
                        else:
                                user_text += event.unicode
                #Checks for backspace
                

        surface.blit(background, (0,0))

        if active:
                color = color_active
        else:
                color = color_passive

        pygame.draw.rect(surface, color, input_rect)
  
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        
        # render at position stated in arguments
        surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)

        #main game logic
        #collison detect
        pygame.display.update()
        
        #For every frame means that at most 30 frames should be passed
        fpsClock.tick(30)

pygame.exit()
