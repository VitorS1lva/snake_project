import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(30, 540)
    y = random.randint(30, 540)
    return(x//10 * 10, y//10 * 10)

def fruit_colision(c1, c2):
    return (c1[0]==c2[0]) and (c1[1]==c2[1])

def wall_colision(c1,c2):
    return (c1[0]==c2[0]) and (c1[1]==c2[1])

UP=0
RIGHT=1
DOWN=2
LEFT=3

pygame.init()
main_screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200, 210), (210,200), (220,200)]
snake_skin=pygame.Surface((10,10))
snake_skin.fill((73, 182, 117))
snake_direction= LEFT
snake_velocity=10
snake_body_velocity=1
snake_body_velocity_dois=0

pear_pos = on_grid_random()
pear=pygame.Surface((10, 10))
pear.fill((51, 115, 63))

apple_pos = on_grid_random()
apple=pygame.Surface((10, 10))
apple.fill((100, 0, 0))

bottom_wall = [(0, 580), (0, 580)]
bottom_wall_skin=pygame.Surface((600,20))
bottom_wall_skin.fill((132, 126, 130))

top_wall = [(0, 0), (0, 0)] 
top_wall_skin=pygame.Surface((600, 20))
top_wall_skin.fill((132, 126, 130))

right_wall = [(580, 0), (580, 0)]
right_wall_skin=pygame.Surface((20, 600))
right_wall_skin.fill((132, 126, 130))

left_wall = [(0, 0), (0, 0)]
left_wall_skin=pygame.Surface((20, 600))
left_wall_skin.fill((132, 126, 130))

clock=pygame.time.Clock()
clock_count=10

while True:
    clock.tick(clock_count)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                snake_direction = UP
            if event.key==K_DOWN:
                snake_direction = DOWN
            if event.key==K_LEFT:
                snake_direction = LEFT
            if event.key==K_RIGHT:
                snake_direction = RIGHT       

    if fruit_colision(snake[0], apple_pos):
        clock_count=clock_count+1
        snake.append((0,0))
        apple_pos=on_grid_random()

    if fruit_colision(snake[0], pear_pos):
        pear_pos=on_grid_random()
        #snake_velocity=snake_velocity+2

    if wall_colision(snake[0], bottom_wall):
        pygame.quit()

    for i in range(len(snake) -1, 0, -1):    
        snake[i]=(snake[i-1][0], snake[i-1][1]) 

    if snake_direction==UP:
        snake[0] = (snake[0][0], snake[0][1]-snake_velocity)
    if snake_direction==DOWN:
        snake[0] = (snake[0][0], snake[0][1]+snake_velocity)
    if snake_direction==RIGHT:
        snake[0] = (snake[0][0]+snake_velocity, snake[0][1])
    if snake_direction==LEFT:
        snake[0] = (snake[0][0]-snake_velocity, snake[0][1])
    
    main_screen.fill((0,0,0))
    main_screen.blit(apple, apple_pos)
    main_screen.blit(pear, pear_pos)
    main_screen.blit(bottom_wall_skin, bottom_wall)
    main_screen.blit(right_wall_skin, right_wall)
    main_screen.blit(left_wall_skin, left_wall)
    main_screen.blit(top_wall_skin, top_wall)
    for pos in snake:
        main_screen.blit(snake_skin, pos)
    
    pygame.display.update()