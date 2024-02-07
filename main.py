#This file contain the functions used in the screen.py script
from random import randint

#Creating the grid
def creat_grid(WID=82, HEI=42):
    return [[0 for _ in range(HEI)] for _ in range(WID)]


#Setting the rules of game of life
def is_alive(grid, pos):
    ngb = []
    ngb += [grid[pos[0]-1][pos[1]-1]]
    ngb += [grid[pos[0]+1][pos[1]-1]]
    ngb += [grid[pos[0]][pos[1]-1]]
    ngb += [grid[pos[0]-1][pos[1]]]
    ngb += [grid[pos[0]+1][pos[1]]]
    ngb += [grid[pos[0]-1][pos[1]+1]]
    ngb += [grid[pos[0]][pos[1]+1]]
    ngb += [grid[pos[0]+1][pos[1]+1]]  
    alives = ngb.count(1)
    
    if grid[pos[0]][pos[1]] == 1:
        if alives == 3 or alives == 2:
            return 1
        else:
            return 0
    else:
        if alives == 3:
            return 1
        else:
            return 0
