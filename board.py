import pygame # type: ignore
import random
import globals
import hand
import card
import util
import asyncio
import time

class Board:

    card_height_width_ratio = 1.4

    def __init__(self, player_hand: hand.Hand, cpu_hand: hand.Hand, grid: list):
        self.player_hand = player_hand
        self.cpu_hand = cpu_hand
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_random_free_space(self):
        row = random.randint(0, self.rows-1)
        col = random.randint(0, self.cols-1)
        if self.grid[row][col] == None:
            return row, col
        return self.get_random_free_space()

    # deprecated
    def players_turn(self):
        player_card = -1
        grid_pos = None
        while player_card == -1 or grid_pos != None:
            player_input = input("Players turn: ")
            player_card, row, col = self.player_hand.play_card(player_input)
            
            grid_pos = self.grid[col][row]

        self.grid[col][row] = player_card

    def cpu_turn(self, screen):
        row, col = self.get_random_free_space()
        card = self.cpu_hand.play_random_card()

        self.grid[row][col] = card
        globals.players_turn = True
        globals.phase = "cpu resolve"
        asyncio.create_task(self.resolve(screen))

    async def resolve(self, screen):
    
        
        await asyncio.sleep(2)

        for row in range(self.rows):
            for col in range(self.cols):
                grid_card = self.grid[row][col]
                left_card = self.grid[row][col-1] if not col == 0 else None
                right_card = self.grid[row][col+1] if not col == self.cols-1 else None
                if grid_card is not None:
                    if grid_card.type == card.Card.Type.predator:
                        if grid_card.hunger <= 1:
                            if left_card is not None and left_card.type == card.Card.Type.prey:
                                left_card.eaten_animation(screen)
                                grid_card.power = grid_card.power + left_card.power
                                self.grid[row][col-1] = None
                                grid_card.hunger = 4
                            elif right_card is not None and right_card.type == card.Card.Type.prey:
                                grid_card.power = grid_card.power + right_card.power
                                self.grid[row][col+1] = None
                                grid_card.hunger = 4
                        
                        if grid_card.hunger == 0:
                            self.grid[row][col] = None
                        else:
                            grid_card.hunger = grid_card.hunger - 1

        if globals.phase == "player resolve":
            globals.phase = "cpu turn"
        else:
            globals.phase = "player turn"

    def display_grid(self, screen):
        card_width = globals.SCREEN_WIDTH*0.07
        card_height = card_width * Board.card_height_width_ratio

        pos_x = globals.SCREEN_WIDTH/2 - card_width*1.1*self.cols/2
        pos_y = globals.SCREEN_HEIGHT/2 - card_height*1.1*self.rows/2

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for row in range(self.rows):
            for col in range(self.cols):
                rel_x = pos_x + card_width*1.1*col
                rel_y = pos_y + card_height*1.1*row
                if mouse_x > rel_x and mouse_x < rel_x + card_width and mouse_y > rel_y and mouse_y < rel_y + card_height:
                    pygame.draw.rect(screen, (150,150,150), (rel_x, rel_y, card_width, card_height))

                    if globals.phase == "player turn" and pygame.mouse.get_pressed()[0] and self.player_hand.selected_card_index is not None:
                        card = self.player_hand.play_card(self.player_hand.selected_card_index, row, col)
                        self.grid[row][col] = card
                        self.player_hand.selected_card_index = None
                        globals.players_turn = False
                        globals.phase = "player resolve"
                        asyncio.create_task(self.resolve(screen))

                else:
                    pygame.draw.rect(screen, (100,100,100), (rel_x, rel_y, card_width, card_height))
                
                if self.grid[row][col] is not None:
                    self.grid[row][col].display_card(rel_x, rel_y, card_width, False, screen)

