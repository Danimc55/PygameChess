import pygame, sys, random
from pygame.locals import *


# global variables
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
FPS = 60

BOARDWIDTH = 8
BOARDHEIGHT = 8

BOXWIDTH = WINDOWWIDTH / BOARDWIDTH
BOXHEIGHT = WINDOWHEIGHT / BOARDHEIGHT


def main():
    global FPSCLOCK, DISPLAYSURF
    # creates a 2D list
    board = []
    for x in range(0, BOARDWIDTH):
        line = []
        for y in range(0, BOARDHEIGHT):
            if (x + y) % 2 == 0:
                line.append((0, 0, 0))
            else:
                line.append((255, 255, 255))
        board.append(line)

    # Pygame initialization
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Ti nisi jedu Keve mi")

    while True: # main game loop
        DISPLAYSURF.fill((0, 0, 0))
        # events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # drawing
        for x, line in enumerate(board):
            for y, box in enumerate(line):
                pygame.draw.rect(DISPLAYSURF, box, (x * BOXWIDTH, y * BOXHEIGHT, BOXWIDTH, BOXHEIGHT))


        # update
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    main()