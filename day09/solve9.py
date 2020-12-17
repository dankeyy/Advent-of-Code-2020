from operator import add
from collections import deque
from itertools import combinations, islice

def getlines(preamable_len=0):
    formatted = lambda x: (int(n) for n in x)

    with open('inp.txt') as lines:
        if preamable_len:
            preamable = islice(lines, preamable_len)
            yield formatted(preamable)
        yield from formatted(lines)


def xmas(preamable_len): #p1
    lines = iter( getlines(preamable_len) )
    deq = deque( next(lines), maxlen=preamable_len )

    for n in lines:
        sumsof2s = { add(*x) for x in combinations(deq, 2) }

        if n in sumsof2s: deq.append(n)
        else: return n


def subsum(goal=138879426): #p2
    lines = list( getlines() )
    l = len(lines)

    for i in range(l):
        total = 0
        for j in range(i, l):
            total += lines[j]
            if total == goal:
                sublist = lines[i: j + 1]
                return min(sublist) + max(sublist)


if __name__ == "__main__":
    print(xmas(25))
    print(subsum())