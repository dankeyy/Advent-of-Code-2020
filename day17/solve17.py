from collections import namedtuple
from itertools import product

ACTIVE, INACTIVE = '#', '.'
Cube = namedtuple('Cube', ['state', 'x', 'y', 'z'])
icube = lambda t, grid: grid[t[0], t[1]] 

# note to self - create a new cube. do not edit your initial one
def get_conway(path='test.txt'):
    with open(path) as lines:
        return [ [c for c in l.rstrip()] for l in lines ]

#c=Cube(x,y,z)
def neighbors(c): 
    adjacent = lambda t1, t2: tuple( sum(x) for x in zip(t1, t2) ) # for adding contents of two tuples
    
    return { adjacent(c, helpers) for helpers in product((0, 1, -1), repeat=3) }


def valid_state(c):
    nearby_actives = sum( n.state == ACTIVE for n in neighbors(c) ) 

    if c.state == ACTIVE: return nearby_actives in {2,3}
    elif c.state == INACTIVE: return nearby_actives != 3


def main():
    conway = get_conway()
    new_conway = [[Cube(c, i, j, 0) for i, c in enumerate(y)] for j, y in enumerate(conway)]

    print(conway)

if __name__ == "__main__":
    #print(get_conway())
    main()