import pygame
import random
import sys

pygame.init()

# create the screen
screen = pygame.display.set_mode((900,600))

# Title and Icon of window
pygame.display.set_caption("Slope Strike")
icon = pygame.image.load('laser-surgery.png')
pygame.display.set_icon(icon)

# background image coordinate plane
gridCP = pygame.image.load('Grid3CP.png')
gridCP2 = pygame.image.load('Grid3CP_level2.png')
gridCP3 = pygame.image.load('Grid3CP_level3.png')
gridCP4 = pygame.image.load('Grid3CP_level4.png')
gridCP5 = pygame.image.load('Grid3CP_level5.png')
UIwindow = pygame.image.load("Card X2.png")
UIwindow = pygame.transform.scale(UIwindow, (300, 600))

amLogo = pygame.image.load("astromechlogo.png")
amLogo = pygame.transform.scale(amLogo, (400, 125))

mainButton = pygame.image.load('button.png')
hoverButton = pygame.image.load('button_hover.png')

viewPort = pygame.image.load('viewport.png')
bridgeMenu = pygame.image.load('bridge.png')
corridorMenu = pygame.image.load('corridor.png')
gameTitle = pygame.image.load('title.png')

upArrow = pygame.image.load("uparrow.png")
upArrow = pygame.transform.scale(upArrow, (50, 50))
downArrow = pygame.image.load("downarrow.png")
downArrow = pygame.transform.scale(downArrow, (50, 50))
rightArrow = pygame.image.load("rightarrow.png")
rightArrow = pygame.transform.scale(rightArrow, (50, 50))
leftArrow = pygame.image.load("leftarrow.png")
leftArrow = pygame.transform.scale(leftArrow, (50, 50))
enterKey = pygame.image.load("blankkey.png")
enterKey = pygame.transform.scale(enterKey, (50, 50))
escKey = pygame.image.load("blankkey.png")
escKey = pygame.transform.scale(escKey, (50, 50))

#Colors
# define the RGB value for colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 215, 255)
red = (255, 0, 0)
orange = (255, 215, 0)
purple = (128, 0, 255)

#Fade function for transitions
def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redrawLogo()
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def redrawLogo():
    screen.fill((0, 0, 0))
    screen.blit(amLogo, (250, 200))
    draw_text(screen, 'Presents', 60, 450, 350, white)

#Text Function
def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('helvetica.ttf'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Load Player and Enemy Images
playerImg = pygame.image.load('ufo.png')
enemyImg = pygame.image.load('alien3.png')
def player(playerImg, playerx, playery):
    screen.blit(playerImg, (playerx, playery))
def enemy(enemyImg, enemyx, enemyy):
    screen.blit(enemyImg, (enemyx, enemyy))

# load level indicator images
#level_img = pygame.image.load('level 2.png')
#levely_change = 10
#level_show = "ready"

# function for showing a level up
#def indicate_level(x, y):
#    global level_show
#    level_show = "on"
#    screen.blit(level_img, (x, y))

# load sound files
def load_sound(file):
    sound = pygame.mixer.Sound(file)
    return sound
laser_sound = load_sound('laser1.mp3')
enemylaser_sound = load_sound('laser1a.mp3')
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
logo_sound = load_sound('R2D2.mp3')
shieldup_sound = load_sound('027.wav')
warning_sound = load_sound('100.wav')
danger_sound = load_sound('015.wav')
lifesupport_sound = load_sound('017.wav')
deflectorfail_sound = load_sound('020.wav')
level5song_sound = load_sound('S31-Going Deep.mp3')


#Function to define locations for Player and Enemy LEVEL 1
def generate_playerandenemy1():
    global enemyx
    global enemyy
    global enemyx_adj
    global enemyy_adj
    global enemyx_expl
    global enemyy_expl
    global playerx
    global playery
    global playerx_adj
    global playery_adj
    enemyx = random.randrange(600, 740, 20)
    enemyy = random.randrange(140, 280, 20)
    enemyx_adj = enemyx / 20 - 29
    enemyy_adj = -1 * (enemyy / 20 - 14)
    enemyx_expl = enemyx - 54
    enemyy_expl = enemyy - 44
    playerx = 580
    playery = 280
    playerx_adj = playerx / 20 - 29
    playery_adj = -1 * (playery / 20 - 14)

#Function to define locations for Player and Enemy LEVEL 2
def generate_playerandenemy2():
    global enemyx
    global enemyy
    global enemyx_adj
    global enemyy_adj
    global enemyx_expl
    global enemyy_expl
    global playerx
    global playery
    global playerx_adj
    global playery_adj
    enemyx = random.randrange(440, 580, 20)
    enemyy = random.randrange(140, 260, 20)
    enemyx_adj = enemyx / 20 - 29
    enemyy_adj = -1 * (enemyy / 20 - 14)
    enemyx_expl = enemyx - 54
    enemyy_expl = enemyy - 44
    playerx = 580
    playery = 280
    playerx_adj = playerx / 20 - 29
    playery_adj = -1 * (playery / 20 - 14)

#Function to define locations for Player and Enemy LEVEL 3
def generate_playerandenemy3():
    global enemyx
    global enemyy
    global enemyx_adj
    global enemyy_adj
    global enemyx_expl
    global enemyy_expl
    global playerx
    global playery
    global playerx_adj
    global playery_adj
    enemyx = random.randrange(440, 560, 20)
    enemyy = random.randrange(280, 420, 20)
    enemyx_adj = enemyx / 20 - 29
    enemyy_adj = -1 * (enemyy / 20 - 14)
    enemyx_expl = enemyx - 54
    enemyy_expl = enemyy - 44
    playerx = 580
    playery = 280
    playerx_adj = playerx / 20 - 29
    playery_adj = -1 * (playery / 20 - 14)

#Function to define locations for Player and Enemy LEVEL 4
def generate_playerandenemy4():
    global enemyx
    global enemyy
    global enemyx_adj
    global enemyy_adj
    global enemyx_expl
    global enemyy_expl
    global playerx
    global playery
    global playerx_adj
    global playery_adj
    enemyx = random.randrange(580, 740, 20)
    enemyy = random.randrange(300, 420, 20)
    enemyx_adj = enemyx / 20 - 29
    enemyy_adj = -1 * (enemyy / 20 - 14)
    enemyx_expl = enemyx - 54
    enemyy_expl = enemyy - 44
    playerx = 580
    playery = 280
    playerx_adj = playerx / 20 - 29
    playery_adj = -1 * (playery / 20 - 14)

#Function to define locations for Player and Enemy LEVEL 5
def generate_playerandenemy5():
    global enemyx
    global enemyy
    global enemyx_adj
    global enemyy_adj
    global enemyx_expl
    global enemyy_expl
    global playerx
    global playery
    global playerx_adj
    global playery_adj
    enemyx = random.randrange(420, 760, 20)
    enemyy = random.randrange(80, 500, 20)
    enemyx_adj = enemyx / 20 - 29
    enemyy_adj = -1 * (enemyy / 20 - 14)
    enemyx_expl = enemyx - 54
    enemyy_expl = enemyy - 44
    playerx = random.randrange(480, 680, 20)
    while playerx == enemyx and playery == enemyy:
        playerx = random.randrange(480, 680, 20)
    playery = random.randrange(80, 480, 20)
    playerx_adj = playerx / 20 - 29
    playery_adj = -1 * (playery / 20 - 14)

#Function for explosion animation
def exploding_function(explosion_type):
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

click = False

# game loops
def main_menu():
    proceed_sound.play()
    menu_sound.play(-1)
    hoverOne = False
    hoverTwo = False
    hoverThree = False
    hoverFour = False
    score = 0
    scores = [0]*6
    running = True
    click = False
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bridgeMenu, (0, 0))
        screen.blit(gameTitle, (100, 150))
        draw_text(screen, 'Created by JP Fletcher and Anthony Tran 2022', 24, 450, 570, orange)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 300, 300, 50)
        button_2 = pygame.Rect(300, 365, 300, 50)
        button_3 = pygame.Rect(300, 430, 300, 50)
        button_4 = pygame.Rect(300, 495, 300, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                campaign_sound.play()
                menu_sound.stop()
                score = campaign()
                scoresTemp = scores
                scoresTemp.append(score)
                scoresTemp.sort(reverse=True)
                scores = [0]*6
                for i in range(6):
                    scores[i]=scoresTemp[i]
        if button_2.collidepoint((mx, my)):
            if click:
                tutorial_sound.play()
                #menu_sound.stop()
                tutorial()
        if button_3.collidepoint((mx, my)):
            if click:
                tutorial_sound.play()
                settings(scores)
        if button_4.collidepoint((mx, my)):
            if click:
                #tutorial_sound.play()
                quit_menu()

        if hoverOne == False:
            screen.blit(mainButton, button_1)
            draw_text(screen, 'START', 64, 450, 305, white)
        else:
            screen.blit(hoverButton, button_1)
            draw_text(screen, 'START', 64, 450, 305, red)
        if hoverTwo == False:
            screen.blit(mainButton, button_2)
            draw_text(screen, 'CONTROLS', 64, 450, 370, white)
        else:
            screen.blit(hoverButton, button_2)
            draw_text(screen, 'CONTROLS', 64, 450, 370, red)
        if hoverThree == False:
            screen.blit(mainButton, button_3)
            draw_text(screen, 'SCORES', 64, 450, 435, white)
        else:
            screen.blit(hoverButton, button_3)
            draw_text(screen, 'SCORES', 64, 450, 435, red)
        if hoverFour == False:
            screen.blit(mainButton, button_4)
            draw_text(screen, 'QUIT', 64, 450, 500, white)
        else:
            screen.blit(hoverButton, button_4)
            draw_text(screen, 'QUIT', 64, 450, 500, red)

        click = False
        for event in pygame.event.get():
            # Check to see if close window is pressed
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            # Check to see if ESC key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    btn1_sound.play()
                    click = True
            if event.type == pygame.MOUSEMOTION:
                if button_1.collidepoint((mx, my)):
                    if hoverOne == False:
                        btn3_sound.play()
                        hoverOne = True
                elif button_2.collidepoint((mx, my)):
                    if hoverTwo == False:
                        btn3_sound.play()
                        hoverTwo = True
                elif button_3.collidepoint((mx, my)):
                    if hoverThree == False:
                        btn3_sound.play()
                        hoverThree = True
                elif button_4.collidepoint((mx, my)):
                    if hoverFour == False:
                        btn3_sound.play()
                        hoverFour = True
                else:
                    hoverOne = False
                    hoverTwo = False
                    hoverThree = False
                    hoverFour = False

        pygame.display.update()

def campaign():
    bridge_sound.play(-1)
    hit_miss_color = (0, 0, 0)
    game_over_1up_color = (0, 0, 0)
    score = 0
    initialScore = score
    multiplier = 1
    lives = 3
    level = 1
    levelx = 680
    levely = 180
    mrise = 0
    mrun = 0
    hit_miss = ''
    game_over_1up = ''
    running = True
    launch = True
    hit = True
    gameOver = False
    global explosion_type
    explosion_type = True
    while running:
        # RGB for background color and background image
        screen.fill((0, 0, 0))

        if level == 1:
            screen.blit(gridCP, (0, 0))
        elif level == 2:
            screen.blit(gridCP2, (0, 0))
        elif level == 3:
            screen.blit(gridCP3, (0, 0))
        elif level == 4:
            screen.blit(gridCP4, (0, 0))
        elif level == 5:
            screen.blit(gridCP5, (0, 0))

        screen.blit(UIwindow, (0, 0))

        # Update HUD, player, and enemy
        if launch == True and hit == True and gameOver == False:
            if level == 5:
                generate_playerandenemy5()
            if level == 4:
                generate_playerandenemy4()
            if level == 3:
                generate_playerandenemy3()
            if level == 2:
                generate_playerandenemy2()
            if level == 1:
                generate_playerandenemy1()
            launch = False
            hit = False
        draw_text(screen, 'RISE', 72, 110, 250, blue)
        draw_text(screen, str(mrise), 72, 220, 250, orange)
        draw_text(screen, 'RUN', 72, 110, 300, blue)
        draw_text(screen, str(mrun), 72, 220, 300, orange)
        draw_text(screen, 'LEVEL', 32, 80, 30, white)
        draw_text(screen, str(level), 64, 80, 65, white)
        draw_text(screen, 'SCORE', 32, 220, 30, white)
        draw_text(screen, str(score), 64, 220, 65, white)
        draw_text(screen, 'SHIELD STRENGTH', 32, 150, 510, white)
        draw_text(screen, str(lives), 64, 150, 535, white)
        draw_text(screen, 'Target lock at coordinates:', 24, 150, 120, white)
        draw_text(screen, '(' + str(int(enemyx_adj)) + ',' + str(int(enemyy_adj)) + ')', 32, 150, 140, white)
        draw_text(screen, 'Launcher location:', 24, 150, 180, white)
        draw_text(screen, '(' + str(int(playerx_adj)) + ',' + str(int(playery_adj)) + ')', 32, 150, 200, white)
        draw_text(screen, hit_miss, 32, 150, 400, hit_miss_color)
        draw_text(screen, game_over_1up, 32, 150, 450, game_over_1up_color)
        enemy(enemyImg, enemyx, enemyy)
        player(playerImg, playerx, playery)
        pygame.display.update()

        # HIT/MISS Calculation
        zerorun = enemyx_adj - playerx_adj
        if launch == True and gameOver == False:
            if mrun != 0:
                draw_laser(playerx, playery, mrise, mrun, enemyx, enemyy)
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
            draw_laser(playerx, playery, mrise, mrun, enemyx, enemyy)
            exploding_function(explosion_type)
            explosion_type = not explosion_type
            game_over_1up = ''
            hit_miss_color = green
            hit_miss = 'HIT!'
            score = 10 * multiplier + score
            if score == 30:
                level = level + 1
            if score == 60:
                level = level + 1
            if score == 90:
                level = level + 1
            if score == 120:
                level = level + 1
                level5song_sound.play(-1)
            if score - initialScore == 60:
                initialScore = score
                lives = lives + 1
                game_over_1up_color = green
                game_over_1up = 'Shield UP!'
                shieldup_sound.play()
            mrun = 0
            mrise = 0
        elif launch == True and hit == False:
            draw_laser(playerx, playery, mrise, mrun, enemyx, enemyy)
            launch = False
            lives = lives - 1
            draw_enemylazer()
            print(f'Current Score: {score}')
            print(f'Shield Level: {lives}')
            if lives == 0:
                # running = False
                level5song_sound.stop()
                deflectorfail_sound.play()
                gameOver = True
                game_over_1up_color = red
                game_over_1up = 'GAME OVER!'
            else:
                danger_sound.play()
                game_over_1up = ''
                hit_miss_color = red
                hit_miss = 'MISS!'

        click = False
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
                    return_menu(click)
                    if return_menu(click) == True:
                        running = False
                        if level == 5:
                            level5song_sound.stop()
                        bridge_sound.stop()
                        menu_sound.play(-1)
                        return score

def tutorial():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(corridorMenu, (0, 0))

        screen.blit(upArrow, (425, 130))
        screen.blit(downArrow, (425, 190))
        screen.blit(rightArrow, (425, 250))
        screen.blit(leftArrow, (425, 310))
        screen.blit(enterKey, (425, 370))
        screen.blit(escKey, (425, 430))
        draw_text(screen, 'Enter', 20, 450, 390, (253, 219, 185))
        draw_text(screen, 'Esc', 20, 450, 450, (253, 219, 185))

        draw_text(screen, 'Key', 70, 250, 80, orange)
        draw_text(screen, 'Key', 70, 250, 80, orange)
        draw_text(screen, 'Function', 70, 650, 80, orange)
        draw_text(screen, 'Up Arrow', 50, 250, 140, blue)
        draw_text(screen, 'Increase RISE', 50, 650, 140, white)
        draw_text(screen, 'Down Arrow', 50, 250, 200, blue)
        draw_text(screen, 'Decrease RISE', 50, 650, 200, white)
        draw_text(screen, 'Right Arrow', 50, 250, 260, blue)
        draw_text(screen, 'Increase RUN', 50, 650, 260, white)
        draw_text(screen, 'Left Arrow', 50, 250, 320, blue)
        draw_text(screen, 'Decrease RUN', 50, 650, 320, white)
        draw_text(screen, 'Enter/Return', 50, 250, 380, blue)
        draw_text(screen, 'Fire laser', 50, 650, 380, white)
        draw_text(screen, 'Escape', 50, 250, 440, blue)
        draw_text(screen, 'Navigate back', 50, 650, 440, white)

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
                    #menu_sound.play(-1)

        pygame.display.update()

def settings(scores):
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(corridorMenu, (0, 0))
        draw_text(screen, 'Rank', 80, 250, 80, orange)
        draw_text(screen, 'Score', 80, 650, 80, orange)
        draw_text(screen, '1st', 60, 250, 140, blue)
        draw_text(screen, str(scores[0]), 60, 650, 140, white)
        draw_text(screen, '2nd', 60, 250, 200, blue)
        draw_text(screen, str(scores[1]), 60, 650, 200, white)
        draw_text(screen, '3rd', 60, 250, 260, blue)
        draw_text(screen, str(scores[2]), 60, 650, 260, white)
        draw_text(screen, '4th', 60, 250, 320, blue)
        draw_text(screen, str(scores[3]), 60, 650, 320, white)
        draw_text(screen, '5th', 60, 250, 380, blue)
        draw_text(screen, str(scores[4]), 60, 650, 380, white)
        draw_text(screen, '6th', 60, 250, 440, blue)
        draw_text(screen, str(scores[5]), 60, 650, 440, white)

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
                    #menu_sound.play(-1)

        pygame.display.update()

def quit_menu():
    running = True
    hoverFive = False
    hoverSix = False
    while running:
        screen.fill((0, 0, 0))
        screen.blit(viewPort, (0, 0))
        draw_text(screen, 'Are you sure you want to quit?', 60, 450, 150, orange)

        mx, my = pygame.mouse.get_pos()

        button_5 = pygame.Rect(100, 300, 300, 50)
        button_6 = pygame.Rect(500, 300, 300, 50)

        if button_5.collidepoint((mx, my)):
            if click:
                quit_sound.play()
                pygame.time.wait(2500)
                pygame.quit()
                sys.exit()
        if button_6.collidepoint((mx, my)):
            if click:
                running = False

        if hoverFive == False:
            screen.blit(mainButton, button_5)
            draw_text(screen, 'YES', 64, 250, 305, white)
        else:
            screen.blit(hoverButton, button_5)
            draw_text(screen, 'YES', 64, 250, 305, red)
        if hoverSix == False:
            screen.blit(mainButton, button_6)
            draw_text(screen, 'NO', 64, 650, 305, white)
        else:
            screen.blit(hoverButton, button_6)
            draw_text(screen, 'NO', 64, 650, 305, red)

        click = False
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    btn1_sound.play()
                    click = True
            if event.type == pygame.MOUSEMOTION:
                if button_5.collidepoint((mx, my)):
                    if hoverFive == False:
                        btn3_sound.play()
                        hoverFive = True
                elif button_6.collidepoint((mx, my)):
                    if hoverSix == False:
                        btn3_sound.play()
                        hoverSix = True
                else:
                    hoverFive = False
                    hoverSix = False

        pygame.display.update()

def return_menu(click):
    running = True
    hoverSeven = False
    hoverEight = False
    while running:
        screen.fill((0, 0, 0))
        screen.blit(viewPort, (0, 0))
        draw_text(screen, 'Are you sure you want to', 60, 450, 120, orange)
        draw_text(screen, 'return to the main menu?', 60, 450, 180, orange)

        mx, my = pygame.mouse.get_pos()

        button_7 = pygame.Rect(100, 300, 300, 50)
        button_8 = pygame.Rect(500, 300, 300, 50)

        if button_7.collidepoint((mx, my)):
            if click:
                return True
        if button_8.collidepoint((mx, my)):
            if click:
                running = False

        if hoverSeven == False:
            screen.blit(mainButton, button_7)
            draw_text(screen, 'YES', 64, 250, 305, white)
        else:
            screen.blit(hoverButton, button_7)
            draw_text(screen, 'YES', 64, 250, 305, red)
        if hoverEight == False:
            screen.blit(mainButton, button_8)
            draw_text(screen, 'NO', 64, 650, 305, white)
        else:
            screen.blit(hoverButton, button_8)
            draw_text(screen, 'NO', 64, 650, 305, red)

        click = False
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    btn1_sound.play()
                    click = True
            if event.type == pygame.MOUSEMOTION:
                if button_7.collidepoint((mx, my)):
                    if hoverSeven == False:
                        btn3_sound.play()
                        hoverSeven = True
                elif button_8.collidepoint((mx, my)):
                    if hoverEight == False:
                        btn3_sound.play()
                        hoverEight = True
                else:
                    hoverSeven = False
                    hoverEight = False

        pygame.display.update()

#lazer boundary testing and firing
def draw_laser(playerx, playery, mrise, mrun, enemyx, enemyy):
    # convert pixel locations to cartesian
    px = playerx / 20 - 29
    py = -1 * (playery / 20 - 14)
    ex = enemyx / 20 - 29
    ey = -1 * (enemyy / 20 - 14)
    # determine coordinates of laser intersection with boundary of coordinate plane
    if mrise != 0 and mrun != 0:
        if mrise > 0 and mrun > 0:
            bx = (mrun / mrise) * (15 - py) + px
            round(bx)
            if bx >= -15 and bx <= 15:
                by = 15
            else:
                bx = 15
                by = (mrise / mrun) * (bx - px) + py
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
            bx = (mrun / mrise) * (15 - py) + px
            round(bx)
            if bx >= -15 and bx <= 15:
                by = 15
            else:
                bx = -15
                by = (mrise / mrun) * (bx - px) + py
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
    elif mrise == 0 and mrun == 0:
        if ey > py:
            bx = px
            by = 15
        else:
            bx = px
            by = -15
    bdryx = 600 + (bx) * 20
    bdryy = 300 + -20 * (by)
    pygame.draw.line(screen, green, (playerx + 20, playery + 20),
                     (bdryx, bdryy), 3)
    pygame.display.flip()
    pygame.time.delay(300)

def draw_enemylazer():
    enemylaser_sound.play()
    pygame.draw.line(screen, red, (enemyx + 20, enemyy + 20),
                     (playerx + 20, playery + 20), 3)
    pygame.display.flip()
    pygame.time.delay(300)

#Load screen stuff
redrawLogo()
pygame.display.update()
pygame.time.delay(3000)
logo_sound.play()
fade(900,600)

main_menu()

                    