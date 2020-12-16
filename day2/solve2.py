from collections import namedtuple

def line_getter(path):
    Line = namedtuple('Line', ['lower', 'upper', 'letter', 'string'])

    with open(path) as lines:
        for line in lines:
            formatting = line.replace('-', ' ').replace(':', '').split() 
            formatting = list( map(int, formatting[0:2]) ) + formatting[2:] #just converting lower&upper to int

            yield Line(*formatting)


def valid1(line_getter):
    for l in line_getter:
        yield l.lower <= l.string.count(l.letter) <= l.upper


def valid2(line_getter):
    for l in line_getter:
        yield (l.string[l.lower - 1] == l.letter) ^ (l.string[l.upper - 1] == l.letter)


if __name__ == "__main__":
   # part 1 
    print( sum( valid1( line_getter('inp.txt') ) ), '-> part1 valids' )
    # part 2
    print( sum( valid2( line_getter('inp.txt') ) ), '-> part2 valids' )