#!/usr/bin/env python

#Import Libraries
import pygame, math, sys
from pygame.locals import *

# Globals
BOARDWIDTH = 10
BOARDHEIGHT = 10
WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
FPS = 30
BLUE = (41, 128, 185)
SHIPS = ['battleship', 'cruiser', 'destroyer', 'submarine', 'dinghy']

def main():
    global FPSCLOCK, SCREEN, BOARDWIDTH, BOARDHEIGHT, WINDOWWIDTH, WINDOWHEIGHT, FPS, BLUE, \
            SHIPS
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Battleship')
    while True:
        run_game()

def run_game():
    """
    This function runs the main event processing loop for the game
    """

    # ----- MAIN PROGRAM LOOP ------ #
    while True:
        SCREEN.fill(BLUE)
        check_for_quit()
        mouse_clicked_flag = False

        # --- MAIN EVENT LOOP ----- #
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                print 'MOUSE BUTTON UP'

        # --- UPDATE SCREEN ----
        pygame.display.update()

        # --- LIMIT TO FPS ----
        FPSCLOCK.tick(FPS)


def generate_board(value):
    """
    Returns a list of 10x10 tiles with value set to value
    """
    board = [[value] * BOARDWIDTH for i in range(BOARDHEIGHT)]
    return board



def check_for_quit():
    for event in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()


#Start everything off
if __name__ == '__main__':
    main()

