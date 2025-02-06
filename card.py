import pygame # type: ignore
import util
import board 

class Card:

    class Type:
        predator = "Predator"
        prey = "Prey"
        tool = "Tool"
        mystical = "Mystical"

    def __init__(self, name: str, type: Type, hunger: int, power: int, player_card: bool):
        self.name = name
        self.hunger = hunger
        self.power = power
        self.type = type
        self.player_card = player_card

    def __str__(self):
        return self.name + " " + self.type + " C:" + str(self.cost) + " P:" + str(self.power)

    def display_card(self, pos_x, pos_y, width, selected, screen):
        
        if self.player_card:
            color = (119, 168, 247)
        else:
            color = (255, 107, 107)

        height = width * board.Board.card_height_width_ratio
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > pos_x and mouse_x < pos_x + width and mouse_y > pos_y and mouse_y < pos_y + height:
            width = width*1.1 
            height = height*1.1
            pos_x = pos_x - width*0.1/2
            pos_y = pos_y - height*0.1/2
        
        if selected:
            pygame.draw.rect(screen, (0,255,0), (pos_x-width*0.05/2, pos_y-height*0.05/2, width*1.05, height*1.05))

        pygame.draw.rect(screen, color, (pos_x, pos_y, width, height))
        font = pygame.font.SysFont("Arial", int(width/6))
        name = font.render(self.name, True, (0,0,0))
        name_w, name_h = font.size(self.name)
        pygame.draw.rect(screen, (255,255,255), (pos_x+width*0.1/2, pos_y + height*0.1 - name_h/2, width*0.9, name_h))
        screen.blit(name, (pos_x + width/2 - name_w/2, pos_y + height*0.1 - name_h/2))

        power_box_x = pos_x+width*0.1/2
        power_box_y = pos_y + height*0.1 + name_h
        power_w, power_h = font.size(str(self.power))
        pygame.draw.rect(screen, (255, 100, 100), (power_box_x, power_box_y, width*0.25, width*0.25))
        power = font.render(str(self.power), True, (0,0,0))
        screen.blit(power, ((power_box_x + width*0.25/2 - power_w/2, power_box_y+width*0.25/2-power_h/2, width*0.25, width*0.25)))
        
        cost_box_x = pos_x+width-width*0.1/2-width*0.25
        cost_box_y = pos_y + height*0.1 + name_h
        cost_w, cost_h = font.size(str(self.hunger))
        pygame.draw.rect(screen, (255, 255, 100), (cost_box_x, cost_box_y, width*0.25, width*0.25))
        power = font.render(str(self.hunger), True, (0,0,0))
        screen.blit(power, ((cost_box_x + width*0.25/2 - cost_w/2, cost_box_y+width*0.25/2-cost_h/2, width*0.25, width*0.25)))

        type_font = pygame.font.SysFont("Arial", int(width/8))
        type = type_font.render(self.type, True, (0,0,0))
        type_w, type_h = type_font.size(self.type)
        pygame.draw.rect(screen, (255,255,255), (pos_x+width*0.1/2, pos_y + height - height*0.1 - type_h/2, width*0.9, type_h))
        screen.blit(type, (pos_x + width/2 - type_w/2, pos_y + height - height*0.1 - type_h/2))
