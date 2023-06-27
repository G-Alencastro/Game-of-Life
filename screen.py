import pygame
from pygame.locals import *
from main import *

def show_grid():
    rect_size = screen_size[0]//(WID-2), screen_size[1]//(HEI-2)
    for x in range(WID):
        for y in range(HEI):
            if GRID[x][y]:   
                pygame.draw.rect(screen, (0, 0, 0), ((x*rect_size[0]+1, y*rect_size[1]+1), (rect_size[0]-1, rect_size[1]-1)))
            else:
                pygame.draw.rect(screen, (255, 255, 255), ((x*rect_size[0]+1, y*rect_size[1]+1), (rect_size[0]-1, rect_size[1]-1)))

pygame.init()

screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size)

running = False
new_grid = []
GRID = creat_grid()
new_grid = creat_grid()

pressed = [0, 0]

fps = 1
clock = pygame.time.Clock()
while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                fps += 1
            if event.key == K_DOWN:
                fps -= 1
            if event.key == 13:
                running = False if running else True
            if event.key == K_f:
                GRID = creat_grid()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pressed[0] = True
            if pygame.mouse.get_pressed()[2]:
                pressed[1] = True
        if event.type == pygame.MOUSEBUTTONUP:
            pressed = [False, False]
        if event.type == QUIT:
            pygame.quit()

    if pressed[0]:
        pos = pygame.mouse.get_pos()
        index = pos[0]//(screen_size[0]//(WID-2)), pos[1]//(screen_size[1]//(HEI-2))
        GRID[index[0]][index[1]] = 1
    if pressed[1]:
        pos = pygame.mouse.get_pos()
        index = pos[0]//(screen_size[0]//(WID-2)), pos[1]//(screen_size[1]//(HEI-2))
        GRID[index[0]][index[1]] = 0

    if running:
        fps = 10
        for x in range(1, WID-1):
            for y in range(1, HEI-1):
                new_grid[x][y] = is_alive(GRID, [x, y])
        GRID = new_grid
        new_grid = creat_grid()

    else:
        fps = -1
    show_grid()

    pygame.display.update()

