from collections import Counter

def get_jolts(path='inp.txt'):
    with open(path) as lines:
        return sorted(map(int, lines))

def p1():
    jolts = get_jolts()
    c = Counter((1,3)).update( jolts[i+1] - jolts[i] for i in range(len(jolts) - 1) )

    return c[1] * c[3]


if __name__ == "__main__":
    print(p1())