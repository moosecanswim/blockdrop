#!/Users/kyleg/miniconda3/bin/python

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

car_width = 73

black = (0, 0, 0)
white = (255, 255, 255)

carImg = pygame.image.load("racecar.png")

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A bit Racey")
clock = pygame.time.Clock()


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged:" + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thing_x, thing_y, thing_w, thing_h, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    # print("in message_display")
    largeText = pygame.font.Font("FreeSansBold.ttf", 115)
    # print("loaded largeText")
    TextSurf, TextRect = text_objects(text, largeText)
    # print("created TextSurf")
    TextRect.center = ((display_width / 2), (display_height / 2))
    # print("set textRect center")
    gameDisplay.blit(TextSurf, TextRect)
    # print("blit that message")

    pygame.display.update()
    print("updated")

    # print("start sleep")
    pygame.time.delay(2000)
    # print("end sleep")


def crash():
    print("in crash method")
    message_display("You Crashed")

    print("restart game loop")
    game_loop()


def game_loop():

    x = display_width * 0.45
    y = display_height * 0.8

    x_change = 0
    y_change = 0
    car_speed = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    thingCount = 1
    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # logic
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                elif event.key == pygame.K_UP:
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    y_change = 10
                elif event.key == pygame.K_r:
                    print("r key pressed")
                    # does not work
                    # carImg = pygame.transform.rotate(carImg, 90)

            if event.type == pygame.KEYUP:
                if (
                    event.key == pygame.K_LEFT
                    or event.key == pygame.K_RIGHT
                    or event.key == pygame.K_UP
                    or event.key == pygame.K_DOWN
                ):
                    x_change = 0
                    y_change = 0

            ######

        x += x_change
        # y += y_change
        gameDisplay.fill(white)

        # block moving
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x, y)

        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        # manage creating a new block
        if thing_starty > display_height:
            print("Create new block")
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += dodged * 1.2

        # check crash from block
        if y < thing_starty + thing_height:
            print("y crossover")

            if (
                x > thing_startx
                and x < thing_startx + thing_width
                or x + car_width > thing_startx
                and x + car_width < thing_startx + thing_width
            ):
                print("x crossover ")
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

