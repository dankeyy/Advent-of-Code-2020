from copy import deepcopy
from itertools import count, takewhile

SEATED, UNSEATED = '#', 'L'


def get_grid(path='test.txt'):
    charsplit = lambda string: [char for char in string]
    with open(path) as f:
        return [charsplit(l.rstrip()) for l in f]


def griddy(grid, tolerance=4):
    new_grid = deepcopy(grid)
    neighbors = {
                    (-1, -1), (0, -1), (1, -1),
                    (-1,  0),          (1,  0),
                    (-1,  1), (0,  1), (1,  1),
                }
    occupied = lambda x: x == SEATED
    empty    = lambda x: x == UNSEATED
    bounded  = lambda x, y: grid[x][y] if x in range( len(grid) ) and y in range( len(grid[0]) ) else None

    for i, r in enumerate(grid):
        for j, c in enumerate(r):

            if empty(c) and all(not occupied(cell) for x, y in neighbors if (cell := bounded(i+x, j+y))): 
                new_grid[i][j] = SEATED

            elif occupied(c) and (sum( occupied(cell) for x, y in neighbors if (cell := bounded(i+x, j+y)) )  >= tolerance):
                new_grid[i][j] = UNSEATED

    return new_grid


def stablize(grid):
    prev = grid
    while (new_grid := griddy(prev)) != prev: prev = new_grid
    return new_grid

idk = lambda grid: (griddy(grid) for _ in count())
stablize = lambda grid: next(g for g in takewhile(lambda grid: grid == idk(grid), idk(grid)))

count_occupied = lambda grid: sum(row.count(SEATED) for row in grid)

if __name__ == "__main__":
    grid = stablize(get_grid('inp.txt'))
    for line in grid: print(''.join(line))
    print(count_occupied(grid))

