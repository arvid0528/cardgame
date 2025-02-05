import pygame # type: ignore
import random
import globals
import board
import util

class Hand:

    def __init__(self, hand: list):
        self.hand = hand
        self.selected_card_index = None

    def play_card(self, card_index, row, col):
        if len(self.hand) > card_index:
            card = self.hand.pop(card_index)
            return card
        return -1
    
    def play_random_card(self, ):
        card = self.hand.pop(random.randint(0, len(self.hand)-1))
        return card

    def display_hand(self, screen):
        card_width = globals.SCREEN_WIDTH * 0.07 * 0.95
        card_height = card_width * board.Board.card_height_width_ratio

        for card_index in range(len(self.hand)):

            mouse_x, mouse_y = pygame.mouse.get_pos()

            pos_x = globals.SCREEN_WIDTH/2 - card_width*1.1*len(self.hand)/2 + card_width*1.1*card_index
            pos_y = globals.SCREEN_HEIGHT - card_height*1.1
            
            if util.mouse_within_rect(mouse_x, mouse_y, pos_x, pos_y, card_width, card_height) and pygame.mouse.get_pressed()[0]:
                self.selected_card_index = card_index
            
            selected = False
            if self.selected_card_index == card_index:
                selected = True

            self.hand[card_index].display_card(pos_x, pos_y, card_width, selected, screen)