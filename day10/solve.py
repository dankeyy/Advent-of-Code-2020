from collections import Counter

def get_jolts(path='test2.txt'):
    with open(path) as lines:
        return sorted(list(map(int, lines)))

def p1():
    jolts = get_jolts()
    c = Counter( l := [jolts[i+1] - jolts[i] for i in range(len(jolts) - 1)] )
    #c = Counter([j-i for i, j in zip(jolts[:-1], jolts[1:])])
    return jolts,l#`c[1] * c[3]


if __name__ == "__main__":
    print(p1())