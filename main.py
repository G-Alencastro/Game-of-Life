from random import randint

WID, HEI =  82, 42
def creat_grid():
    return [[0 for _ in range(HEI)] for _ in range(WID)]

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


if __name__ == '__main__':
    c =  [[0, 1, 2, 3],
          [4, 5, 6, 7], 
          [8, 9, 10, 11]]
    ngb = []
    pos = [1, 2]

    ngb += [c[pos[0]-1][pos[1]-1]]
    ngb += [c[pos[0]-1][pos[1]]]
    ngb += [c[pos[0]-1][pos[1]+1]]

    ngb += [c[pos[0]+1][pos[1]-1]]
    ngb += [c[pos[0]+1][pos[1]]]
    ngb += [c[pos[0]+1][pos[1]+1]]  

    ngb += [c[pos[0]][pos[1]-1]]
    ngb += [c[pos[0]][pos[1]+1]]
    print(ngb)