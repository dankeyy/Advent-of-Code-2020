from itertools import islice
from math import prod


def trees(right, down):
    with open('inp.txt') as lines:
        for i, line in enumerate( islice(lines, down, None, down), start = 1):
                    yield '#' == line[ (i * right) % len( line.strip() ) ]


if __name__ == "__main__":
    #part 1
    p1sum = sum(trees(3,1)) 
    print(p1sum, '-> part1')
    
    #part2
    directions = ( (1,1), (3, 1), (5, 1), (7, 1), (1, 2) )
    p2sum = prod( ( sum(trees(*i)) for i in directions ) )
    print(p2sum, '-> part 2')