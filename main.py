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

#Player Draw Function
playerImg = pygame.image.load('ufo.png')
def player(playerImg, playerx, playery):
    screen.blit(playerImg, (playerx, playery))

#Enemy Draw Function
enemyImg = pygame.image.load('alien3.png')
def enemy(enemyImg, enemyx, enemyy):
    screen.blit(enemyImg, (enemyx, enemyy))

#load sound files
def load_sound(file):
    sound = pygame.mixer.Sound(file)
    return sound
laser_sound = load_sound('laser1.mp3')
explosion_sound1 = load_sound('explosion1.wav')
explosion_sound2 = load_sound('explosion2.wav')
btn1_sound = load_sound('brdgbtn1.wav')
btn2_sound = load_sound('brdgbtn5.wav')
btn3_sound = load_sound('brdgbtn3.wav')
btn4_sound = load_sound('brdgbtn6.wav')
bridge_sound = load_sound('bridge.wav')
proceed_sound = load_sound('061.wav')
menu_sound = load_sound('eprd-bridge.wav')
campaign_sound = load_sound('211.wav')
tutorial_sound = load_sound('226.wav')
quit_sound = load_sound('014.wav')

click = False

# game loops
def main_menu():
    proceed_sound.play()
    menu_sound.play(-1)
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, 'SLOPE STRIKE!', 120, 450, 150, orange)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 300, 300, 50)
        button_2 = pygame.Rect(300, 400, 300, 50)
        button_3 = pygame.Rect(300, 500, 300, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                campaign_sound.play()
                menu_sound.stop()
                campaign()
        if button_2.collidepoint((mx, my)):
            if click:
                tutorial_sound.play()
                tutorial()
                menu_sound.stop()
        if button_3.collidepoint((mx, my)):
            if click:
                quit_sound.play()
                pygame.time.wait(2500)
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
    bridge_sound.play(-1)
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
    explosion_type = True
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
                enemyx_expl = enemyx - 54
                enemyy_expl = enemyy - 44

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
                    draw_laser(playerx, playery, mrise, mrun)
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
                explosion_sprite10 = [pygame.image.load('expl_10_000.png'), pygame.image.load('expl_10_001.png'),
                                    pygame.image.load('expl_10_002.png'), pygame.image.load('expl_10_003.png'),
                                    pygame.image.load('expl_10_004.png'), pygame.image.load('expl_10_005.png'),
                                    pygame.image.load('expl_10_006.png'), pygame.image.load('expl_10_007.png'),
                                    pygame.image.load('expl_10_008.png'), pygame.image.load('expl_10_009.png'),
                                    pygame.image.load('expl_10_0010.png'), pygame.image.load('expl_10_0011.png'),
                                    pygame.image.load('expl_10_0012.png'), pygame.image.load('expl_10_0013.png'),
                                    pygame.image.load('expl_10_0014.png'), pygame.image.load('expl_10_0015.png'),
                                    pygame.image.load('expl_10_0016.png'), pygame.image.load('expl_10_0017.png'),
                                    pygame.image.load('expl_10_0018.png'), pygame.image.load('expl_10_0019.png'),
                                    pygame.image.load('expl_10_0020.png'), pygame.image.load('expl_10_0021.png'),
                                    pygame.image.load('expl_10_0022.png'), pygame.image.load('expl_10_0023.png'),
                                    pygame.image.load('expl_10_0024.png'), pygame.image.load('expl_10_0025.png'),
                                    pygame.image.load('expl_10_0026.png'), pygame.image.load('expl_10_0027.png'),
                                    pygame.image.load('expl_10_0028.png'), pygame.image.load('expl_10_0029.png'),
                                    pygame.image.load('expl_10_0030.png'), pygame.image.load('expl_10_0031.png')]
                explosion_sprite06 = [pygame.image.load('expl_06_000.png'), pygame.image.load('expl_06_001.png'),
                                    pygame.image.load('expl_06_002.png'), pygame.image.load('expl_06_003.png'),
                                    pygame.image.load('expl_06_004.png'), pygame.image.load('expl_06_005.png'),
                                    pygame.image.load('expl_06_006.png'), pygame.image.load('expl_06_007.png'),
                                    pygame.image.load('expl_06_008.png'), pygame.image.load('expl_06_009.png'),
                                    pygame.image.load('expl_06_0010.png'), pygame.image.load('expl_06_0011.png'),
                                    pygame.image.load('expl_06_0012.png'), pygame.image.load('expl_06_0013.png'),
                                    pygame.image.load('expl_06_0014.png'), pygame.image.load('expl_06_0015.png'),
                                    pygame.image.load('expl_06_0016.png'), pygame.image.load('expl_06_0017.png'),
                                    pygame.image.load('expl_06_0018.png'), pygame.image.load('expl_06_0019.png'),
                                    pygame.image.load('expl_06_0020.png'), pygame.image.load('expl_06_0021.png'),
                                    pygame.image.load('expl_06_0022.png'), pygame.image.load('expl_06_0023.png'),
                                    pygame.image.load('expl_06_0024.png'), pygame.image.load('expl_06_0025.png'),
                                    pygame.image.load('expl_06_0026.png'), pygame.image.load('expl_06_0027.png'),
                                    pygame.image.load('expl_06_0028.png'), pygame.image.load('expl_06_0029.png'),
                                    pygame.image.load('expl_06_0030.png'), pygame.image.load('expl_06_0031.png')]
                draw_laser(playerx, playery, mrise, mrun)
                if explosion_type == True:
                    explosion_value = 1
                    explosion_sound1.play()
                    while explosion_value < len(explosion_sprite06):
                        explosion_image = explosion_sprite06[explosion_value]
                        screen.blit(explosion_image, (enemyx_expl + 50, enemyy_expl + 30))
                        pygame.display.update()
                        explosion_value += 1
                        pygame.time.delay(50)
                else:
                    explosion_value = 1
                    explosion_sound2.play()
                    while explosion_value < len(explosion_sprite10):
                        explosion_image = explosion_sprite10[explosion_value]
                        screen.blit(explosion_image, (enemyx_expl, enemyy_expl))
                        pygame.display.update()
                        explosion_value += 1
                        pygame.time.delay(30)
                explosion_type = not explosion_type
                game_over_1up = ''
                hit_miss_color = green
                hit_miss = 'HIT!'
                score = score + 10
                mrun = 0
                mrise = 0
                if score - initialScore == 100:
                    initialScore = score
                    lives = lives + 1
                    game_over_1up_color = green
                    game_over_1up = '1 UP!'
            elif launch == True and hit == False:
                draw_laser(playerx, playery, mrise, mrun)
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
                        btn1_sound.play()
                        if mrun > -20:
                            mrun = mrun - 1
                    elif event.key == pygame.K_RIGHT:
                        btn2_sound.play()
                        if mrun < 20:
                            mrun = mrun + 1
                    elif event.key == pygame.K_UP:
                        btn3_sound.play()
                        if mrise < 20:
                            mrise = mrise + 1
                    elif event.key == pygame.K_DOWN:
                        btn4_sound.play()
                        if mrise > -20:
                            mrise = mrise - 1
                    elif event.key == pygame.K_RETURN:
                        laser_sound.play()
                        launch = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        bridge_sound.stop()
                        menu_sound.play(-1)

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
                    menu_sound.play(-1)

        pygame.display.update()

#lazer boundary testing and firing
def draw_laser(playerx, playery, mrise, mrun):
    #convert pixel locations to cartesian
    px = playerx / 20 - 29
    py = -1 * (playery / 20 - 14)
    #determine coordinates of laser intersection with boundary of coordinate plane
    if mrise != 0 and mrun != 0:
         if mrise > 0 and mrun > 0:
             bx = (mrun/mrise) * (15 - py) + px
             round(bx)
             if bx >= -15 and bx <=15:
                by = 15
             else:
                bx = 15
                by = (mrise/mrun) * (bx - px) + py
                round(by)
         elif mrise < 0 and mrun < 0:
             bx = (mrun / mrise) * (-15 - py) + px
             round(bx)
             if bx >= -15 and bx <= 15:
                by = -15
             else:
                bx = -15
                by = (mrise / mrun) * (bx - px) + py
                round(by)
         elif mrise > 0 and mrun < 0:
                bx = (mrun/mrise) * (15 - py) + px
                round(bx)
                if bx >= -15 and bx <=15:
                    by = 15
                else:
                    bx = -15
                    by = (mrise/mrun) * (bx-px) + py
                    round(by)
         elif mrise < 0 and mrun > 0:
                bx = (mrun / mrise) * (-15 - py) + px
                round(bx)
                if bx >= -15 and bx <= 15:
                    by = -15
                else:
                    bx = 15
                    by = (mrise / mrun) * (bx - px) + py
                    round(by)
    elif mrise == 0 and mrun != 0:
         if mrun > 0:
             bx = 15
             by = py
         else:
             bx = -15
             by = py
    elif mrise != 0 and mrun == 0:
         if mrise > 0:
             bx = px
             by = 15
         else:
             bx = px
             by = -15
    bdryx = 600 + (bx)* 20
    bdryy = 300 + -20*(by)
    pygame.draw.line(screen, green, (playerx + 20, playery + 20),
                     (bdryx, bdryy), 3)
    pygame.display.flip()
    pygame.time.delay(300)

main_menu()

                    