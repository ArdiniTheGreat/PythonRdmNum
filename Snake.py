# -*- coding: utf-8 -*-




#import modules

import pygame

import random

import time

from time import sleep

def collision_with_snake(snake_head, snake_position):
    for box in snake_position[1:]:
        if snake_head[0] == box[0] and snake_head[1] == box[1]:
            return 1
    return 0
def collision_with_boundaries(snake_head):

    # if snake is outside of boundaries return 1
    if snake_head[0]>=display_width or snake_head[0]<0 or snake_head[1]>=display_height or snake_head[1]<0:
        return 1
    else:
        return 0
def generate_snake(snake_head, snake_position, button_direction, grow_counter):
    
    #uses button_direction to decide where snake head will go
    if button_direction == 1:
        snake_head[0] += 10
    elif button_direction == 0:
        snake_head[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10
        
    snake_position.insert(0,list(snake_head))  
    if (grow_counter % 20 == 0):
        grow_counter = grow_counter
    else:
        snake_position.pop()
        
    return snake_position    
def display_snake(snake_position):

    #uses list of snake's positions to display snake
    for position in snake_position:
        pygame.draw.rect(display,player_color,pygame.Rect(position[0],position[1],10,10))
def play_game(snake_head, snake_position, button_direction,grow_counter):

    crashed = False
    
    while crashed is not True:

        for event in pygame.event.get():

            #ends game if you click on X
            if event.type == pygame.QUIT:
                crashed = True
            #sets variable used to move snake using arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button_direction = 0
                elif event.key == pygame.K_RIGHT:
                    button_direction = 1
                elif event.key == pygame.K_UP:
                    button_direction = 3
                elif event.key == pygame.K_DOWN:
                    button_direction = 2
    


        #moves snake position
        snake_position = generate_snake(snake_head, snake_position, button_direction, grow_counter)
         

        #display background and snake
        display.fill(window_color)
        display_snake(snake_position)
        pygame.display.update()
        

        #ends game loop if snake leaves the boundary
        if collision_with_boundaries(snake_head) == 1 or collision_with_snake(snake_head, snake_position) == 1:
            crashed = True
        #snake grow counter
        grow_counter = grow_counter - 1
        
        clock.tick(20)



if __name__ == "__main__":

    # set variables

    display_width = 1000

    display_height = 900

    player_color = (255,255,0)

    window_color = (0,0,0)
    
    grow_counter = 5

    clock=pygame.time.Clock()

    #create the snake

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250]]



    #initialize pygame modules    

    pygame.init()

    

    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game")

    pygame.display.update()

    

    #start the game loop

    play_game(snake_head, snake_position, 1, grow_counter)



    pygame.quit()