#!/home/qwerty/virtualenvironment/env/bin/python

from tabulate import tabulate
from itertools import product
from copy import deepcopy

def getlines(path='inp.txt'):
    charsplit = lambda string: [char for char in string]
    with open(path) as lines:
        return [charsplit(l.rstrip('\n')) for l in lines] # returns fully occupied grid


def look_around(x, y, grid): # returns seats pending for check
    current = grid[x][y]
    edge = len(grid) - 1
    seats = set()
    
    if current == '.' : return # corners 

    elif (x, y) == (0, 0): seats = { (0, 1), (1, 1), (1, 0) } 

    elif (x, y) == (edge, 0): seats = { (edge - 1, 0), (edge - 1, 1), (edge, 1) }

    elif (x, y) == (0, edge): seats = { (0, edge - 1), (1, edge), (1, edge -1) }

    elif (x, y) == (edge, edge): seats = { (edge, edge - 1), (edge - 1, edge), (edge - 1, edge - 1) }

    elif x == 0: seats = { (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x + 1, y) } # left-most column
    
    elif x == edge: seats = { (x, y + 1), (x, y - 1), (x - 1, y + 1), (x - 1, y - 1), (x - 1, y) } # right-most column
    
    elif y == 0: seats = { (x + 1, y), (x - 1, y), (x + 1, y + 1), (x - 1, y + 1), (x, y + 1) } # up-most row
    
    elif y == edge: seats = { (x + 1, y), (x - 1, y), (x + 1, y - 1), (x - 1, y - 1), (x, y - 1) } # down-most row
    
    else: seats = { (x + 1, y), (x - 1, y), (x + 1, y - 1), (x - 1, y - 1), (x, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x, y + 1) } # all-around

    return seats


def change(grid, action): # action: 0 for try to clear all. 1 for try to seat all
    cell = lambda a, b: grid[a][b]
    clone = deepcopy(grid)
    needs_to_sit_down = lambda x, y, seats: grid[x][y] == 'L' and all(cell(*i) != '#' for i in seats)
    needs_to_stand_up = lambda x, y, seats: grid[x][y] == '#' and sum(cell(*i) == '#' for i in seats) >= 4

    swappable = {0: needs_to_stand_up, 1: needs_to_sit_down}
    swap = {'#':'L', 'L': '#'}

    for x, y in product(range( len(grid) ), repeat=2):
            seats = look_around(x, y, grid)

            if seats and swappable[action] (x, y, seats):
                clone[x][y] = swap[grid[x][y]]
    return clone


def count_occupied(grid):
    return sum(row.count('#') for row in grid)


def stablize(grid):
    nexty = lambda x: change( change(x, 1), 0)
    prev = nexty(grid)

    while prev != nexty(prev):
        prev = nexty(prev)
    
    return nexty(prev)


if __name__ == "__main__":
    lines = getlines('inp.txt')
    lines = stablize(lines)
    for line in lines: print(''.join(line))
    print(count_occupied(lines))