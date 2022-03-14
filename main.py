import pygame
import random

# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *
# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode([900,600])

# Title and Icon of window
pygame.display.set_caption("Slope Strike")
icon = pygame.image.load('laser-surgery.png')
pygame.display.set_icon(icon)

#background image coordinate plane
gridCP = pygame.image.load('Grid3CP.png')
UIwindow = pygame.image.load("Card X2.png")
UIwindow = pygame.transform.scale(UIwindow, (300, 600))

#Colors
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 215, 255)
red = (255, 0, 0)
orange = (255, 215, 0)
hit_miss_color = (0, 0, 0)
game_over_1up_color = (0, 0, 0)

# Text Function
def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('freesansbold.ttf'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Player
playerImg = pygame.image.load('ufo.png')
def player(playerImg, playerx, playery):
    screen.blit(playerImg, (playerx, playery))

# Enemy
enemyImg = pygame.image.load('alien3.png')
#enemyImg = pygame.transform.scale(enemyImg, (20, 20))
def enemy(enemyImg, enemyx, enemyy):
    screen.blit(enemyImg, (enemyx, enemyy))

print('Greetings user. Prepare to SlopeStrike!')

# Game Loop
score = 0
initialScore = score
lives = 3
mrise = 0
mrun = 0
hit_miss = ''
game_over_1up = ''
running = True
launch = True
hit = True
gameOver = False

while running:
        # RGB for background color and background image
        screen.fill((0, 0, 0))
        screen.blit(gridCP, (0, 0))
        screen.blit(UIwindow, (0,0))

        # Text
        draw_text(screen, 'RISE', 72, 110, 250, blue)
        draw_text(screen, str(mrise), 72, 220, 250, orange)
        draw_text(screen, 'RUN', 72, 110, 300, blue)
        draw_text(screen, str(mrun), 72, 220, 300, orange)
        draw_text(screen, 'SCORE', 32, 150, 30, white)
        draw_text(screen, str(score), 64, 150, 55, white)
        draw_text(screen, 'LIVES', 32, 150, 510, white)
        draw_text(screen, str(lives), 64, 150, 535, white)

        # Text-based SlopeStrikeApp
        if launch == True and hit == True and gameOver == False:
            # Generate and print two random points, a target, enemyxy, and a Launch location, playerxy
            enemyx = random.randrange(400, 800, 20)
            enemyy = random.randrange(100, 400, 20)
            enemyx_adj = enemyx / 20 - 29
            enemyy_adj = -1 * (enemyy / 20 - 14)

            playerx = random.randrange(560, 600, 20)
            playery = random.randrange(260, 300, 20)
            playerx_adj = playerx / 20 - 29
            playery_adj = -1 * (playery / 20 - 14)
            launch = False
            hit = False

        enemy(enemyImg, enemyx, enemyy)
        player(playerImg, playerx, playery)

        draw_text(screen, 'Target lock at coordinates:', 24, 150, 120, white)
        draw_text(screen, '(' + str(int(enemyx_adj)) + ',' + str(int(enemyy_adj)) + ')', 32, 150, 140, white)

        draw_text(screen, 'Launcher location:', 24, 150, 180, white)
        draw_text(screen, '(' + str(int(playerx_adj)) + ',' + str(int(playery_adj)) + ')', 32, 150, 200, white)

        draw_text(screen, hit_miss, 32, 150, 400, hit_miss_color)
        draw_text(screen, game_over_1up, 32, 150, 450, game_over_1up_color)

        pygame.display.update()

        #print(f'Target lock at coordinates ({enemyx_adj},{enemyy_adj}).')
        #print(f'Launcher location: ({playerx_adj},{playery_adj}).')

        # Prompts user for two inputs to form a ratio
        # mrise = int(input("Enter the appropriate rise:"))
        # mrun = int(input("Enter the approriate run:"))
        # print(f'You entered {mrise}/{mrun}.')

        # Verifies if the inputted slope forms a line that intersects the Launch and Target locations
        zerorun = enemyx_adj - playerx_adj
        if launch == True and gameOver == False:
            if mrun != 0:
                if (enemyy_adj - playery_adj) == (enemyx_adj - playerx_adj) * (mrise / mrun):
                    hit = True
                else:
                    hit = False
            else:
                if zerorun == 0:
                    hit = True
                else:
                    hit = False

        if launch == True and hit == True:
            game_over_1up = ''
            print(f'HIT!')
            hit_miss_color = green
            hit_miss = 'HIT!'
            score = score + 10
            print(f'Current Score: {score}')
            print(f'Lives: {lives}')
            if score - initialScore == 100:
                initialScore = score
                lives = lives + 1
                game_over_1up_color = green
                game_over_1up = '1 UP!'
        elif launch == True and hit == False:
            launch = False
            lives = lives - 1
            print(f'Current Score: {score}')
            print(f'Lives: {lives}')
            if lives == 0:
                # running = False
                gameOver = True
                print(f'Game Over. Final Score: {score}')
                game_over_1up_color = red
                game_over_1up = 'GAME OVER!'
            else:
                game_over_1up = ''
                print(f'MISS!')
                hit_miss_color = red
                hit_miss = 'MISS!'

        # Check to see if close window is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        # Arrow keys to change rise and run values, and Enter key to launch
            elif event.type == pygame.KEYDOWN and gameOver == False:
                if event.key == pygame.K_LEFT:
                    if mrun > -20:
                        mrun = mrun - 1
                elif event.key == pygame.K_RIGHT:
                    if mrun < 20:
                        mrun = mrun + 1
                elif event.key == pygame.K_UP:
                    if mrise < 20:
                        mrise = mrise + 1
                elif event.key == pygame.K_DOWN:
                    if mrise > -20:
                        mrise = mrise - 1
                elif event.key == pygame.K_RETURN:
                    launch = True