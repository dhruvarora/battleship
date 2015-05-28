#!/usr/bin/env python

#Import Libraries
import pygame, math, sys
from pygame.locals import *
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

BOARDHEIGHT = 10
BOARDWIDTH = 10

def main():
    pygame.init()
    pygame.display.set_caption('Battleship')
    print(generate_board(False))



def generate_board(value):
    """
    Returns a list of 10x10 tiles with value set to value
    """
    board = [[value] * BOARDWIDTH for i in range(BOARDHEIGHT)]
    return board

#Start everything off
if __name__ == '__main__':
    main()

