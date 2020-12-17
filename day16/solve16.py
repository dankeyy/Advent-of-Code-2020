import re
from itertools import takewhile

def ranges(path='ranges.txt'):
    pattern = re.compile(r'(\d+)-(\d+)')
    ao = lambda x, y: (x, y + 1)
    s = set()

    with open(path) as lines:
        for line in lines:
            for rng in re.findall(pattern, line):
                for n in range( *ao( *map(int, rng) ) ):
                    s.add(n)
    return s


def nearby_tickets(ranges, path='nearby_tickets.txt'):
    with open(path) as lines:
        for line in lines: 
            for n in map(int, line.rstrip().split(',')):
                if n not in ranges:
                    yield n


if __name__ == "__main__":
    print( sum( nearby_tickets( ranges() ) ) )