import pygame
import random
import sys

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
# green, blue color .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 215, 255)
red = (255, 0, 0)
orange = (255, 215, 0)
purple = (128, 0, 255)

#Text Function
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

# This old print was for the textbased version. Consider printing some instructions in a future version.
#print('Greetings user. Prepare to SlopeStrike!')

click = False

# game loops
def main_menu():
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, 'SLOPE STRIKE!', 120, 450, 150, orange)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 300, 300, 50)
        button_2 = pygame.Rect(300, 400, 300, 50)
        button_3 = pygame.Rect(300, 500, 300, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                campaign()
        if button_2.collidepoint((mx, my)):
            if click:
                tutorial()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, purple, button_1)
        draw_text(screen, 'CAMPAIGN', 64, 450, 305, white)
        pygame.draw.rect(screen, purple, button_2)
        draw_text(screen, 'TUTORIAL', 64, 450, 405, white)
        pygame.draw.rect(screen, purple, button_3)
        draw_text(screen, 'QUIT', 64, 450, 505, white)

        click = False
        for event in pygame.event.get():
            # Check to see if close window is pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
            # Check to see if ESC key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def campaign():
    hit_miss_color = (0, 0, 0)
    game_over_1up_color = (0, 0, 0)
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

    #Spawn player and enemy
            enemy(enemyImg, enemyx, enemyy)
            player(playerImg, playerx, playery)

    #Update HUD with current coordinates
            draw_text(screen, 'Target lock at coordinates:', 24, 150, 120, white)
            draw_text(screen, '(' + str(int(enemyx_adj)) + ',' + str(int(enemyy_adj)) + ')', 32, 150, 140, white)

            draw_text(screen, 'Launcher location:', 24, 150, 180, white)
            draw_text(screen, '(' + str(int(playerx_adj)) + ',' + str(int(playery_adj)) + ')', 32, 150, 200, white)

    #Draw the GREEN hit or the RED miss
            draw_text(screen, hit_miss, 32, 150, 400, hit_miss_color)
    #Draw the RED game over or the GREEN 1up
            draw_text(screen, game_over_1up, 32, 150, 450, game_over_1up_color)

            pygame.display.update()


            # Prompts user for two inputs to form a ratio
            # mrise = int(input("Enter the appropriate rise:"))
            # mrun = int(input("Enter the approriate run:"))
            # print(f'You entered {mrise}/{mrun}.')

            # Verifies if the inputed slope forms a line that intersects the Launch and Target locations
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
                hit_miss_color = green
                hit_miss = 'HIT!'
                score = score + 10
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
                    game_over_1up_color = red
                    game_over_1up = 'GAME OVER!'
                else:
                    game_over_1up = ''
                    hit_miss_color = red
                    hit_miss = 'MISS!'

            # Check to see if close window is pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            # Arrow keys to change rise and run values, and Enter key to launch
                if event.type == pygame.KEYDOWN and gameOver == False:
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

def tutorial():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text(screen, 'TUTORIAL', 120, 450, 150, orange)

        for event in pygame.event.get():
            # Check to see if close window is pressed
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            # Check to see if ESC key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()

main_menu()

                    