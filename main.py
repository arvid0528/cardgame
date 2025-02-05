import random
import pygame # type: ignore
import util
from board import Board
from hand import Hand
from card import Card
import globals

def main():

    player_wolf = Card("Wolf", Card.Type.animal, 3, 4, True)
    player_sheep = Card("Sheep", Card.Type.animal, 1, 2, True)
    cpu_wolf = Card("Wolf", Card.Type.animal, 3, 4, False)
    cpu_sheep = Card("Sheep", Card.Type.animal, 1, 2, False)

    player_hand = Hand([player_wolf, player_wolf, player_sheep, player_sheep, player_sheep])
    cpu_hand = Hand([cpu_wolf, cpu_sheep, cpu_sheep, cpu_sheep, cpu_sheep])

    cols = 8
    rows = 3
    
    grid = [[None for i in range(cols)] for j in range(rows)]

    board = Board(player_hand, cpu_hand, grid)

    pygame.init()
    screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((50, 50, 50))

        board.display_grid(screen)
        board.player_hand.display_hand(screen)

        if not globals.players_turn:
            board.cpu_turn()

        pygame.display.flip()   

    pygame.quit()


if __name__ == "__main__":
    main()