import random
import pygame # type: ignore
import util
from board import Board
from hand import Hand
from card import Card
from globals import *

def main():

    wolf = Card("Wolf", Card.Type.animal, 3, 4)
    sheep = Card("Sheep", Card.Type.animal, 1, 2)

    player_hand = Hand([wolf, wolf, sheep, sheep, sheep])
    cpu_hand = Hand([wolf, sheep, sheep, sheep, sheep])

    cols = 4
    rows = 2

    grid = [[None for i in range(cols)] for j in range(rows)]

    board = Board(player_hand, cpu_hand, grid)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    running = True

    global players_turn

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((50, 50, 50))

        players_turn = True

        board.display_grid(screen)
        board.player_hand.display_hand(screen)

        pygame.display.flip()   

    pygame.quit()


if __name__ == "__main__":
    main()