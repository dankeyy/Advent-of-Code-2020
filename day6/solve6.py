from itertools import chain

def groups(gfile = 'inp.txt'):
    group = []

    with open(gfile) as lines:
        for line in chain(lines, '\n'):
            if line != '\n': 
                group.append( line.strip() )
                
            else:
                yield group
                group.clear()

if __name__ == "__main__":
    #part 1
    print( sum( len(group) for group in groups() ), '--> part1 sum-counts' )
    #part 2
    intersections = lambda x: len( set(x[0]).intersection(*x[1:]) )
    print( sum( intersections(group) for group in groups() ), '--> part2 sum-counts' )