import pygame
import os
import random
from pygame import *
pygame.font.init()
pygame.init()

# Settings
width, height = 350, 350
screen = display.set_mode((width, height))
display.set_caption("Fly Bot Adventures: Quest for the Coins")

white = (255, 255, 255)
black = (0, 0, 0)
lightblue = (182, 222, 229)
red = (255, 0, 0)

score_font = pygame.font.SysFont('times new roman', 20)
lives_font = pygame.font.SysFont('times new roman', 20)

FPS = 60

side_spaceship_width, side_spaceship_height = 75, 70
middle_spaceship_width, middle_spaceship_height = 70, 65

move_up = False
move_down = False
move_left = False
move_right = False

coin_hit = pygame.USEREVENT + 1
black_ship_hit = pygame.USEREVENT + 2
blue_ship_hit = pygame.USEREVENT + 3
green_ship_hit = pygame.USEREVENT + 4
orange_ship_hit = pygame.USEREVENT + 5

# Sprites
fly_bot_start = pygame.image.load(os.path.join('FlyBot Assets', 'fly_bot.png'))
fly_bot_image = pygame.transform.scale(fly_bot_start, (35, 40))
coin_start = pygame.image.load(os.path.join('FlyBot Assets', 'coin.png'))
coin_image = pygame.transform.scale(coin_start, (20, 20))
black_ship_start = pygame.image.load(os.path.join('FlyBot Assets', 'blackship0.png'))
black_ship_image = pygame.transform.scale(black_ship_start, (middle_spaceship_width, middle_spaceship_height))
blue_ship_start = pygame.image.load(os.path.join('FlyBot Assets', 'blueship.png'))
blue_ship_image = pygame.transform.scale(blue_ship_start, (middle_spaceship_width, middle_spaceship_height))
green_ship_start = pygame.image.load(os.path.join('FlyBot Assets', 'greenship0.png'))
green_ship_image = pygame.transform.scale(green_ship_start, (side_spaceship_width, side_spaceship_height))
orange_ship_start = pygame.image.load(os.path.join('FlyBot Assets', 'orangeship0.png'))
orange_ship_image = pygame.transform.scale(orange_ship_start, (side_spaceship_width, side_spaceship_height))


# Methods
def draw_window(bot, coin, score, lives, black_ship, blue_ship, green_ship, orange_ship):
    screen.fill(lightblue)
    score_text = score_font.render("Score: " + str(score), 1, black)
    lives_text = lives_font.render("Lives: " + str(lives), 1, black)
    screen.blit(score_text, (5, 5))
    screen.blit(lives_text, (94, 5))
    screen.blit(fly_bot_image, (bot.x, bot.y))
    screen.blit(coin_image, (coin.x, coin.y))
    screen.blit(black_ship_image, (black_ship.x, black_ship.y))
    screen.blit(blue_ship_image, (blue_ship.x, blue_ship.y))
    screen.blit(green_ship_image, (green_ship.x, green_ship.y))
    screen.blit(orange_ship_image, (orange_ship.x, orange_ship.y))
    display.update()


def ship_movement(black_ship, blue_ship, green_ship, orange_ship, black_ship_vel, blue_ship_vel, green_ship_vel,
                  orange_ship_vel):
    black_ship.y -= black_ship_vel
    if black_ship.y <= -60:
        black_ship.x = random.randint(5, 345-middle_spaceship_width)
        black_ship.y = 415
    blue_ship.y += blue_ship_vel
    if blue_ship.y >= 400:
        blue_ship.x = random.randint(5, 345-middle_spaceship_width)
        blue_ship.y = -80
    green_ship.x += green_ship_vel
    if green_ship.x >= 355:
        green_ship.x = -80
        green_ship.y = random.randint(5, 345-side_spaceship_height)
    orange_ship.x -= orange_ship_vel
    if orange_ship.x <= -80:
        orange_ship.x = 400
        orange_ship.y = random.randint(5, 345-side_spaceship_height)


def handle_black_ship(bot, black_ship):
    if bot.colliderect(black_ship):
        pygame.event.post(pygame.event.Event(black_ship_hit))
        black_ship.x = random.randint(5, 345-middle_spaceship_width)
        black_ship.y = 415


def handle_blue_ship(bot, blue_ship):
   if bot.colliderect(blue_ship):
       pygame.event.post(pygame.event.Event(blue_ship_hit))
       blue_ship.x = random.randint(5, 345-middle_spaceship_width)
       blue_ship.y = -80


def handle_green_ship(bot, green_ship):
   if bot.colliderect(green_ship):
       pygame.event.post(pygame.event.Event(green_ship_hit))
       green_ship.x = -80
       green_ship.y = random.randint(5, 345-side_spaceship_height)


def handle_orange_ship(bot, orange_ship):
   if bot.colliderect(orange_ship):
       pygame.event.post(pygame.event.Event(orange_ship_hit))
       orange_ship.x = 355
       orange_ship.y = random.randint(5, 345-side_spaceship_height)


def handle_coin(bot, coin):
    if bot.colliderect(coin):
       pygame.event.post(pygame.event.Event(coin_hit))
       coin.x = random.randint(25, 325)
       coin.y = random.randint(25, 325)


# Sprite Creation and More Variables
bot = pygame.Rect(width/2-17.5, 125, 35, 40)
coin = pygame.Rect(width/2-10, 50, 20, 20)
black_ship = pygame.Rect(width/2-35, 350, middle_spaceship_width, middle_spaceship_height)
blue_ship = pygame.Rect(width/2-35, -80, middle_spaceship_width, middle_spaceship_height)
green_ship = pygame.Rect(-80, 135, side_spaceship_width, side_spaceship_height)
orange_ship = pygame.Rect(350, 135, side_spaceship_width, side_spaceship_height)
up_vel = 4
down_vel = 2
left_vel = 1.25
right_vel = 2.25
black_ship_vel = 2
blue_ship_vel = 2.25
green_ship_vel = 2.50
orange_ship_vel = 2
gravity = 2.5
score = 0
lives = 25
clock = time.Clock()
run = True
while run:
    clock.tick(FPS)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_down = False
                move_up = True
            if event.key == pygame.K_DOWN:
                move_up = False
                move_down = True
            if event.key == pygame.K_LEFT:
                move_right = False
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_left = False
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False

        if event.type == black_ship_hit:
            lives -= 1

        if event.type == blue_ship_hit:
            lives -= 1

        if event.type == green_ship_hit:
            lives -= 1

        if event.type == orange_ship_hit:
            lives -= 1

        if event.type == coin_hit:
            score += 1

    # Updates
    if move_up and bot.y > 0:
        bot.y -= up_vel
    if move_down and bot.y + down_vel + bot.height < height:
        bot.y += down_vel
    if move_left and bot.x - left_vel > 0:
        bot.x -= left_vel
    if move_right and bot.x + bot.width < width:
        bot.x += right_vel
    if bot.y + gravity + bot.height < height:
        bot.y += gravity

    ship_movement(black_ship, blue_ship, green_ship, orange_ship, black_ship_vel, blue_ship_vel, green_ship_vel,
                  orange_ship_vel)
    handle_black_ship(bot, black_ship)
    handle_blue_ship(bot, blue_ship)
    handle_green_ship(bot, green_ship)
    handle_orange_ship(bot, orange_ship)
    handle_coin(bot, coin)
    if lives == 0:
        run = False
    # Draw
    draw_window(bot, coin, score, lives, black_ship, blue_ship, green_ship, orange_ship)