from collections import Counter
from functools import lru_cache

with open('inp.txt') as lines:
    adapters = sorted( map(int, lines) )
    jolts = [0] + adapters + [adapters[-1] + 3]


def p1():
    c = Counter(jolts[i+1] - jolts[i] for i in range(len(jolts) - 1))
    return c[1] * c[3]


@lru_cache
def p2(i=0):
    if i == (len(jolts) - 1): return 1
    return sum( p2(x) for x in range( i + 1, len(jolts) ) if jolts[x] - jolts[i] <= 3 )


if __name__ == "__main__":
    print( p1() )
    print( p2() )