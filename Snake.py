# -*- coding: utf-8 -*-




#import modules

import pygame

import random

import time

from time import sleep
def enemy_collision_with_boundaries(comsnake1_head):

    # if snake is outside of boundaries return 1
    if comsnake1_head[0]>=display_width or comsnake1_head[0]<0 or comsnake1_head[1]>=display_height or comsnake1_head[1]<0:
        return 1
    else:
        return 0
def enemy_collision(comsnake1_head, snake_position):
    for box in snake_position:
        if comsnake1_head[0] == box[0] and comsnake1_head[1] == box[1]:
            return 1
    return 0
def collision_with_enemy(snake_head, comsnake1_position):
    for box in comsnake1_position:
        if snake_head[0] == box[0] and snake_head[1] == box[1]:
            return 1
    return 0
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
def generate_comsnake(comsnake1_head, comsnake1_position, grow_counter,snake_head,distance_counter,button_direction2,player2):
    xdistance = comsnake1_head[0] - snake_head[0]
    ydistance = comsnake1_head[1] - snake_head[1]
    if player2 == 2:
        if button_direction2 == 1:
            comsnake1_head[0] += 10
        elif button_direction2 == 0:
            comsnake1_head[0] -= 10
        elif button_direction2 == 2:
            comsnake1_head[1] += 10
        elif button_direction2 == 3:
            comsnake1_head[1] -= 10        
    elif player2 == 1:
        if distance_counter % 5 == 0:
            random_path = random.randint(1,4)
            if (random_path == 1):    
                    comsnake1_head[0] -= 10
            elif (random_path == 2):
                    comsnake1_head[0] += 10
            elif (random_path == 3):
                    comsnake1_head[1] -= 10
            elif (random_path == 4):
                    comsnake1_head[1] += 10        
        elif (xdistance)>0 and abs(xdistance)>abs(ydistance):
            comsnake1_head[0] -= 10
        elif (xdistance)<0 and abs(xdistance)>abs(ydistance):
            comsnake1_head[0] += 10
        elif (ydistance)>0 and abs(ydistance)>abs(xdistance):
            comsnake1_head[1] -= 10
        elif (ydistance)<0 and abs(ydistance)>abs(xdistance):
            comsnake1_head[1] += 10  
    comsnake1_position.insert(0,list(comsnake1_head))  
    if (grow_counter % 20 == 0):
        grow_counter = grow_counter 
    else:
        comsnake1_position.pop()
         
    return comsnake1_position    
    
def display_snake(snake_position):

    #uses list of snake's positions to display snake
    for position in snake_position:
        pygame.draw.rect(display,player_color,pygame.Rect(position[0],position[1],10,10))

def display_comsnake(comsnake1_position):
    for position in comsnake1_position:
        pygame.draw.rect(display,comsnake_color,pygame.Rect(position[0],position[1],10,10))
        
def play_game(snake_head, snake_position, button_direction,grow_counter,comsnake1_head,comsnake1_position,distance_counter,p1score,comscore,player2):

    crashed = False
    button_direction2 = 0
    
    while crashed is not True:

        for event in pygame.event.get():
            
            #ends game if you click on X
            if event.type == pygame.QUIT:
                if p1score>comscore:
                    print("You Won! " + " Player: " +str(p1score)+ " Computer: " +str(comscore))
                elif comscore>p1score:
                    print("You Lost!" + "Player: " +str(p1score)+ " Computer: " +str(comscore))
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
            if player2 == 2:
                if event.key == pygame.KEYDOWN:
                    if event.key == pygame.K_KP4:
                        button_direction2 = 0
                    elif event.key == pygame.K_KP6:
                        button_direction2 = 1
                    elif event.key == pygame.K_KP8:
                        button_direction2 = 3
                    elif event.key == pygame.K_KP2:
                        button_direction2 = 2            

        #moves snake position
        snake_position = generate_snake(snake_head, snake_position, button_direction, grow_counter)
        
        comsnake1_position = generate_comsnake(comsnake1_head, comsnake1_position, grow_counter,snake_head,distance_counter,button_direction2,player2)

        #display background and snake
        display.fill(window_color)
        display_snake(snake_position)
        display_comsnake(comsnake1_position)
        pygame.display.update()
        #kills enemy snake
        if enemy_collision(comsnake1_head, snake_position) == 1:
            snake_head = [100,50]
            snake_position = [[100,50],[50,50],[0,50]]
            comsnake1_head = [900,850]
            comsnake1_position = [[900,850],[850,850],[800,850]]
            p1score = p1score + 1
        #ends game loop if snake leaves the boundary
        if collision_with_boundaries(snake_head) == 1 or collision_with_snake(snake_head, snake_position) == 1 or collision_with_enemy(snake_head, comsnake1_position) == 1:
            snake_head = [100,50]
            snake_position = [[100,50],[50,50],[0,50]]
            comsnake1_head = [900,850]
            comsnake1_position = [[900,850],[850,850],[800,850]]
            comscore = comscore + 1
        #snake grow counter
        grow_counter = grow_counter - 1
        
        #comsnake AI distance clock
        distance_counter = distance_counter - 1
        
        clock.tick(20)



if __name__ == "__main__":

    # set variables

    display_width = 1000

    display_height = 900

    player_color = (255,255,0)
    
    comsnake_color = (0,255,0)

    window_color = (0,0,0)
    
    grow_counter = 5

    clock=pygame.time.Clock()
    
    distance_counter = 0
    
    p1score = 0
    
    comscore = 0

    #create the snake

    snake_head = [100,50]

    snake_position = [[100,50],[50,50],[0,50]]

    comsnake1_head = [900,850]
    
    comsnake1_position = [[900,850],[850,850],[800,850]]

    #initialize pygame modules    

    pygame.init()

    player2 = input("1p or 2p? 1 for 1p, 2 for 2p;")

    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game")

    pygame.display.update()

    

    #start the game loop

    play_game(snake_head, snake_position, 1, grow_counter,comsnake1_head,comsnake1_position,distance_counter,p1score,comscore,player2)



    pygame.quit()