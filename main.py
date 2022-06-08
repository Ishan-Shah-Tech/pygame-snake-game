from random import randrange


# Simple pygame program

# Import and initialize the pygame library
import pygame
from random import randrange

print("Snake by Ishan Shah")
print("Have fun!")

# COLOR = (R, G, B) = (RED, GREEN, BLUE)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# PIXEL = look at the screen really close, you'll see a dot
SCREEN_SIZE = (500, 500)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

# GAME VARIABLES
GAME_STATE = True
MOUSE_POS = pygame.mouse.get_pos()


# FUNCTIONS:
def drawCircle(x, y, radius, color):
    pygame.draw.circle(SCREEN, color, (x, y), radius)

LOCATION_X = 0
LOCATION_Y = 0

while GAME_STATE == True:
    pygame.display.flip()

    drawCircle(LOCATION_X, LOCATION_Y, 50, RED)    

    for event in pygame.event.get():
        drawCircle(LOCATION_X, LOCATION_Y, 50, BLACK)    
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_LEFT:
            LOCATION_X = LOCATION_X - 10                
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_RIGHT:
            LOCATION_X = LOCATION_X + 10            
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_UP:
            LOCATION_Y = LOCATION_Y - 10    
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_DOWN:
            LOCATION_Y = LOCATION_Y + 10                      
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_ESCAPE:
            GAME_STATE = False
        drawCircle(LOCATION_X, LOCATION_Y, 50, RED)           

pygame.quit()

# HOMEWORK:
# stage the changes in git using:
    # git add .
# commit the changes in git using:
    # git commit -m "I AM ADDING CHANAGES HERE TO MOVE A CIRCLE"
# push the changes to the game using 
    # git push origin pygame-sname-game
