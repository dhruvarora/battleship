#!/usr/bin/env python

#Import Libraries
import pygame, math, sys
import random
from pygame.locals import *

# Globals
BOARDWIDTH = 10
BOARDHEIGHT = 10
WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
FPS = 30
BLUE = (41, 128, 185)
SHIPS = ['battleship', 'cruiser', 'destroyer', 'dinghy', 'carrier']

def main():
    global FPSCLOCK, SCREEN, BOARDWIDTH, BOARDHEIGHT, WINDOWWIDTH, WINDOWHEIGHT, FPS, BLUE, \
            SHIPS
    
    # --- INIT ----
    pygame.init()

    # --- CONSTANTS ---
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Battleship')

    # --- RUN GAME ---
    while True:
        run_game()

def run_game():
    """
    This function runs the main event processing loop for the game
    """
    mouseX, mouseY = 0,0
    board = generate_board(None, False)
    board = add_ships(board, SHIPS)
    print board

    # ----- MAIN PROGRAM LOOP ------ #
    while True:
        SCREEN.fill(BLUE)
        check_for_quit()
        mouse_clicked_flag = False

        # --- MAIN EVENT LOOP ----- #
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos


        # --- UPDATE SCREEN ----
        pygame.display.update()

        # --- LIMIT TO FPS ----
        FPSCLOCK.tick(FPS)


def generate_board(shipName, shotValue):
    """
    Returns a list of list of tuples with each tuple containing shipName, and 
    shotStatus.
    """
    board = [[[shipName, shotValue]] * BOARDWIDTH for i in range(BOARDHEIGHT)]
    return board


def add_ships(board, ships):
    '''
    Returns a board with ships added.
    @param: Input board, List of ships.
    This is currently our "AI" brain
    '''
    final_board = board[:]
    ship_length = 0
    for ship in ships:
        valid_ship_position = False
        while not valid_ship_position:
            xCoord = random.randint(0, 9)
            yCoord = random.randint(0, 9)
            orientation = random.randint(0, 1)
            if 'carrier' in ship:
                ship_length = 5
            elif 'battleship' in ship:
                ship_length = 4
            elif 'destroyer' in ship:
                ship_length = 3
            elif 'cruiser' in ship:
                ship_length = 2
            elif 'dinghy' in ship:
                ship_length = 1

            valid_ship_position, ship_coordinates = validate_ship(final_board,
                    xCoord, yCoord, orientation, ship, ship_length)
            if valid_ship_position:
                for coordinate in ship_coordinates:
                    final_board[coordinate[0]][coordinate[1]][0] = ship
    return final_board

def validate_ship(board, xC, yC, orientation, ship, length):
    ship_coordinates = []
    if orientation:
        for i in range(length):
            if (i + xC > 9) or (board[i + xC][yC][0] != None):
                return (False, ship_coordinates)
            else:
                ship_coordinates.append((i+xC, yC))
    else:
        for i in range(length):
            if (i + yC > 9) or (board[xC][i + yC][0] != None):
                return (False, ship_coordinates)
            else:
                ship_coordinates.append((xC, i + yC))
    return (True, ship_coordinates)


def draw_board():
    """
    Draws the board
    """



def check_for_quit():
    for event in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()


#Start everything off
if __name__ == '__main__':
    main()

