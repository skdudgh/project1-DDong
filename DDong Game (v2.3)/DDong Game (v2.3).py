import pygame
import random
import os
import subprocess
pygame.init()

SILVER = (192, 192, 192)
PURPLE = (128, 0, 128)
NAVY = (0, 0, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTNAVY = (0, 128, 128)
OLIVE = (128, 128, 0)
GREEN = (0, 128, 0)
LIME = (0, 255, 0)
YELLOW = (225,225, 0)
MAGENTA = (225, 0, 225)
bonus = random.randint(0, 300)

bonus_score = None

screen_width = 500
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NEW POO GAME (v.2)")
screen.fill(BLACK)

current = os.path.dirname(__file__)
image = os.path.join(current, "image")
sound = os.path.join(current, "sound")
rule_and_control = os.path.join(current, "information")

rule_and_control_path = os.path.join(rule_and_control, "how_to_play.txt")

logo = pygame.image.load(os.path.join(image, "logo.png"))
pygame.display.set_icon(logo)

start = pygame.image.load(os.path.join(image, "start.png"))
start_rect = start.get_rect()
start_size = start.get_rect().size
start_width = start_size[0]
start_height = start_size[1]

start_x_pos = (screen_width / 2 - start_width/2)
start_y_pos = (screen_height / 2 - start_height/2)
start_click = False

money = pygame.image.load(os.path.join(image, "money.png"))
money = pygame.transform.scale(money, (50,50))
money_rect = money.get_rect()
money_size = money.get_rect().size
money_width = money_size[0]
money_height = money_size[1]
money_x_pos = random.randint(0, 450)
money_y_pos = random.randint(0, 50)

ddong1 = pygame.image.load(os.path.join(image, "ddong.png"))
ddong1 = pygame.transform.scale(ddong1, (50,50))
ddong1_rect = ddong1.get_rect()
ddong1_size = ddong1.get_rect().size
ddong1_width = ddong1_size[0]
ddong1_height = ddong1_size[1]

ddong2 = pygame.image.load(os.path.join(image, "ddong.png"))
ddong2 = pygame.transform.scale(ddong2, (50,50))
ddong2_rect = ddong2.get_rect()
ddong2_size = ddong2.get_rect().size
ddong2_width = ddong2_size[0]
ddong2_height = ddong2_size[1]

ddong3 = pygame.image.load(os.path.join(image, "ddong.png"))
ddong3 = pygame.transform.scale(ddong3, (50,50))
ddong3_rect = ddong3.get_rect()
ddong3_size = ddong3.get_rect().size
ddong3_width = ddong3_size[0]
ddong3_height = ddong3_size[1]

ddong4 = pygame.image.load(os.path.join(image, "ddong.png"))
ddong4 = pygame.transform.scale(ddong4, (50,50))
ddong4_rect = ddong4.get_rect()
ddong4_size = ddong4.get_rect().size
ddong4_width = ddong4_size[0]
ddong4_height = ddong4_size[1]

ddong1_x_pos = random.randint(0, 450)
ddong1_y_pos = random.randint(0, 50)
ddong2_x_pos = random.randint(0, 450)
ddong2_y_pos = random.randint(0, 50)
ddong3_x_pos = random.randint(0, 450)
ddong3_y_pos = random.randint(0, 50)
ddong4_x_pos = random.randint(0, 450)
ddong4_y_pos = random.randint(0, 50)

player = pygame.image.load(os.path.join(image, "player.png"))
player = pygame.transform.scale(player, (75,75))
player_rect = player.get_rect()
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]

player_x_pos = (screen_width / 2 - player_width/2)
player_y_pos = (screen_height - player_height)

gameBGM = pygame.mixer.Sound(os.path.join(sound, "Rainy_Waltz.mp3"))
gameBGM.set_volume(0.015)

font = pygame.font.SysFont( "arial", 30, True, False)
score = 0

fall=False
ready = False
over = False
add = 10
life = 5

died_message_x_pos = ((screen_width / 2) - 50)
died_message_y_pos = ((screen_height / 2) - 80)

ddong1_speed = 0.25
ddong2_speed = 0.21
ddong3_speed = 0.27
ddong4_speed = 0.3
money_speed = 0.312

moveX = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.get_rel()
            mouse_pos = pygame.mouse.get_pos()
            if not start_click:
                if mouse_pos[0] > 154 and mouse_pos[0] < 346 and mouse_pos[1] > 321.5 and mouse_pos[1] < 378.5:
                    start_click = True        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX -= 0.25
            if event.key == pygame.K_RIGHT:
                moveX += 0.25
            if event.key == pygame.K_SPACE:
                subprocess.run(["notepad.exe",rule_and_control_path])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                moveX = 0
    
    display_score = font.render("money : {}".format(str(score)), False, WHITE)
    end_score = font.render("Total score : {}".format(str(score+bonus)), False, WHITE)
    life_display = font.render("life : {}".format(str(life)), False, SILVER)
    died_message = font.render("You Died", False, RED)
    inform = font.render("[Press SPACE] -> HOW TO PLAY", False, WHITE)

    mark1 = font.render("mark : F", False, PURPLE)
    mark2 = font.render("mark : E", False, NAVY)
    mark3 = font.render("mark : D", False, LIGHTNAVY)
    mark4 = font.render("mark : C", False, OLIVE)
    mark5 = font.render("mark : B", False, GREEN)
    mark6 = font.render("mark : A", False, LIME)
    mark7 = font.render("mark : A+", False, MAGENTA)
    mark8 = font.render("mark : A++", False, YELLOW)

    player_x_pos += moveX

    if player_x_pos <= 0:
        player_x_pos = 0
    if player_x_pos >= screen_width - player_width:
        player_x_pos = screen_width - player_width

    if ready:
        if ddong1_x_pos <= player_x_pos <= ddong1_x_pos + 50 and player_y_pos <= ddong1_y_pos + 50:
            ready = False
            over = True
            life -= 1
        if ddong2_x_pos <= player_x_pos <= ddong2_x_pos + 50 and player_y_pos <= ddong2_y_pos + 50:
            ready = False
            over = True
            life -= 1
        if ddong3_x_pos <= player_x_pos <= ddong3_x_pos + 50 and player_y_pos <= ddong3_y_pos + 50:
            ready = False
            over = True
        if ddong4_x_pos <= player_x_pos <= ddong4_x_pos + 50 and player_y_pos <= ddong4_y_pos + 50:
            ready = False
            over = True
            life -= 1
        if ddong1_x_pos - 50 <= player_x_pos <= ddong1_x_pos and player_y_pos <= ddong1_y_pos + 50:
            ready = False
            over = True
            life -= 1
        if ddong2_x_pos - 50 <= player_x_pos <= ddong2_x_pos and player_y_pos <= ddong2_y_pos + 50:
            ready = False
            over = True
            life -= 1
        if ddong3_x_pos - 50 <= player_x_pos <= ddong3_x_pos and player_y_pos <= ddong3_y_pos + 50:
            ready = False
            over = True
            life -= 1
        if ddong4_x_pos - 50 <= player_x_pos <= ddong4_x_pos and player_y_pos <= ddong4_y_pos + 50:
            ready = False
            over = True
            life -= 1
        if money_x_pos <= player_x_pos <= money_x_pos + 50 and player_y_pos <= money_y_pos + 50:
            score += add
            money_x_pos = random.randint(0, 450)
            money_y_pos = random.randint(0, 50)
            bonus_score = random.randint(1, 6)
            score += bonus_score
            bonus_score = None
        if money_x_pos - 50 <= player_x_pos <= money_x_pos and player_y_pos <= money_y_pos + 50:
            score += add
            money_x_pos = random.randint(0, 450)
            money_y_pos = random.randint(0, 50)
            bonus_score = random.randint(1, 6)
            score += bonus_score
            bonus_score = None

    screen.blit(start, (start_x_pos, start_y_pos))
    screen.blit(inform, (0, 650))
    screen.blit(life_display, (400, 10))

    if ddong1_x_pos == ddong2_x_pos:
        ddong1_x_pos = random.randint(0, 450)
    if ddong1_x_pos == ddong3_x_pos:
        ddong1_x_pos = random.randint(0, 450)
    if ddong1_x_pos == ddong4_x_pos:
        ddong1_x_pos = random.randint(0, 450)
    if ddong2_x_pos == ddong3_x_pos:
        ddong2_x_pos = random.randint(0, 450)
    if ddong2_x_pos == ddong4_x_pos:
        ddong2_x_pos = random.randint(0, 450)
    if ddong3_x_pos == ddong4_x_pos:
        ddong3_x_pos = random.randint(0, 450)

    if over:
        gameBGM.stop()
        ddong1_speed = 0
        ddong2_speed = 0
        ddong3_speed = 0
        ddong4_speed = 0
        money_speed = 0
        ddong1_y_pos = random.randint(0, 50)
        ddong2_y_pos = random.randint(0, 50)
        ddong3_y_pos = random.randint(0, 50)
        ddong4_y_pos = random.randint(0, 50)
        money_y_pos = random.randint(0, 50)
        screen.fill(BLACK)
        screen.blit(start, (start_x_pos, start_y_pos))
        screen.blit(display_score, (0, 0))
        life_display.set_alpha(0)
        start_click = False
        over = False
        ready = False

    if start_click:
            ready = True
            screen.fill(BLACK)
            if ready:
                gameBGM.play()
                screen.blit(player, (player_x_pos, player_y_pos))
                screen.blit(ddong1, (ddong1_x_pos, ddong1_y_pos))
                screen.blit(ddong2, (ddong2_x_pos, ddong2_y_pos))
                screen.blit(ddong3, (ddong3_x_pos, ddong3_y_pos))
                screen.blit(ddong4, (ddong4_x_pos, ddong4_y_pos))
                screen.blit(money, (money_x_pos, money_y_pos))
                screen.blit(display_score, (0, 0))
                fall = True
                ddong1_speed = 0.25
                ddong2_speed = 0.21
                ddong3_speed = 0.27
                ddong4_speed = 0.3
                money_speed = 0.312

    if not over:
        if fall:
            money_y_pos += money_speed
            ddong1_y_pos += ddong1_speed
            ddong2_y_pos += ddong2_speed
            ddong3_y_pos += ddong3_speed
            ddong4_y_pos += ddong4_speed
            if ddong1_y_pos >= 700:
                ddong1_x_pos = random.randint(0, 450)
                ddong1_y_pos = random.randint(0, 50)
            if ddong2_y_pos >= 700:
                ddong2_x_pos = random.randint(0, 450)
                ddong2_y_pos = random.randint(0, 50)
            if ddong3_y_pos >= 700:
                ddong3_x_pos = random.randint(0, 450)
                ddong3_y_pos = random.randint(0, 50)
            if ddong4_y_pos >= 700:
                ddong4_x_pos = random.randint(0, 450)
                ddong4_y_pos = random.randint(0, 50)
            if money_y_pos >= 1400:
                money_x_pos = random.randint(0, 450)
                money_y_pos = random.randint(0, 50)

    if life <= 0:
        screen.fill(BLACK)
        screen.blit(died_message, (died_message_x_pos, died_message_y_pos))
        over = True
        start_click = False
        gameBGM.stop()
        if score <= 150:
            screen.blit(mark1, (died_message_x_pos + 5, died_message_y_pos + 40))
            screen.blit(end_score, (250, 640))
        if 150 < score <= 300:
            screen.blit(mark2, (died_message_x_pos + 5, died_message_y_pos + 40))
            screen.blit(end_score, (250, 640))
        if 300 < score <= 450:
            screen.blit(mark3, (died_message_x_pos +5, died_message_y_pos + 40))
            screen.blit(end_score, (250, 640))
        if 450 < score <= 600:
            screen.blit(mark4, (died_message_x_pos + 5, died_message_y_pos + 40))
            screen.blit(end_score, (250, 640))
        if 600 < score <= 750:
            screen.blit(mark5, (died_message_x_pos + 5, died_message_y_pos + 40))
            screen.blit(end_score, (250, 640))
        if 750 < score <= 900:
            screen.blit(mark6, (died_message_x_pos + 5, died_message_y_pos + 40))
            screen.blit(end_score, (250, 640))
        if 900 < score <= 1200:
            screen.blit(mark7, (died_message_x_pos + 5, died_message_y_pos + 40))
            screen.blit(end_score, (250, 640))
        if score > 1200:
            screen.blit(mark8, (died_message_x_pos + 5, died_message_y_pos + 40))
            screen.blit(end_score, (250, 640))
        if start_click:
            gameBGM.stop()
            over = True
            start_click = False

    screen.blit(life_display, (400, 10))
            
    pygame.display.update()
pygame.quit()