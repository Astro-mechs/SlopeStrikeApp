import pygame
import random

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((900,600))

# Title and Icon of window
pygame.display.set_caption("Slope Strike")
icon = pygame.image.load('laser-surgery.png')
pygame.display.set_icon(icon)

#background image coordinate plane
gridCP = pygame.image.load('Grid3CP.png')
UIwindow = pygame.image.load("Card X2.png")
UIwindow = pygame.transform.scale(UIwindow, (300, 600))

# Player
playerImg = pygame.image.load('ufo.png')
def player(x, y):
    screen.blit(playerImg, (playerx, playery))
    pygame.display.flip()

# Enemy
enemyImg = pygame.image.load('alien3.png')
#enemyImg = pygame.transform.scale(enemyImg, (20, 20))
def enemy(x, y):
    screen.blit(enemyImg, (enemyx, enemyy))
    pygame.display.flip()

# Game Loop
running = True
while running:

    # RGB for background color and background image
    screen.fill((0, 0, 0))
    screen.blit(gridCP, (0, 0))
    screen.blit(UIwindow, (0,0))

    # check to see if close window is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Textbased SlopeStrikeApp

    print ('Greetings user. Prepare to SlopeStrike!')

    score = 0
    lives = 3
    while lives > 0:

        # Generate and print two random points, a target, Txy, and a Launch location, Lxy
        enemyx = random.randrange(400, 800, 20)
        enemyy = random.randrange(100, 400, 20)
        playerx = random.randrange(560, 600, 20)
        playery = random.randrange(260, 300, 20)
        enemyx_adj = enemyx/20 - 29
        enemyy_adj = -1*(enemyy/20 - 14)
        playerx_adj = playerx/20 - 29
        playery_adj = -1*(playery/20 - 14)
        player(playerx, playery)
        enemy(enemyx, enemyy)
        pygame.display.update()
        print(f'Target lock at coordinates ({enemyx_adj},{enemyy_adj}).')
        print(f'Launcher location: ({playerx_adj},{playery_adj}).')

        # Prompts user for two inputs to form a ratio
        mrise = int(input("Enter the appropriate rise:"))
        mrun = int(input("Enter the approriate run:"))
        print(f'You entered {mrise}/{mrun}.')

        # Verifies if the inputted slope forms a line that intersects the Launch and Target locations
        zerorun = enemyx_adj - playerx_adj
        if (zerorun == 0 and mrun == 0) or (enemyy_adj) - (playery_adj) == ((enemyx_adj) - (playerx_adj)) * (mrise) / (mrun):
            print(f'HIT!')
            score = score + 10
            print(f'Current Score: {score}')
        else:
            print(f'MISS!')
            lives = lives - 1
            print(f'Current Score: {score}')

    print(f'Game Over. Final Score: {score}')