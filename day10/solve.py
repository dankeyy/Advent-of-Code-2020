from collections import Counter
from functools import lru_cache

with open('inp.txt') as lines:
    adapters = sorted( map(int, lines) )
    jolts = [0] + adapters + [adapters[-1] + 3]

diffs = [ jolts[i+1] - jolts[i] for i in range(len(jolts) - 1) ]


def p1():
    c = Counter(diffs)
    return c[1] * c[3]

@lru_cache
def p2(i=0):
    if i == (len(jolts) - 1): return 1
    total=0
    for x in range(i + 1, len(jolts)):
        if 1 <= jolts[x] - jolts[i] <= 3:
            total += p2(x)

    return total


if __name__ == "__main__":
    # print( p1() )
    print(p2())