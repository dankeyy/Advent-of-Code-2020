import re
from operator import add, mul
from copy import deepcopy

opr = {'+': add, '*': mul}
evaluate = lambda x, n1, n2: opr[x](n1, n2)

def parse_calc(txt):
    for i in re.finditer(r'((\d+) (\W) (\d+))', txt):
        _, n1, x, n2 = i.groups()
        indexes = i.span()

        yield indexes, (x, *map( int, (n1, n2) ) )

def parse_brackets(txt):
    for i in re.finditer(r'\(\d+\)', txt):
        yield *i.span(), i.string[1:-1]

def main(txt):
    # clone = deepcopy(txt)
    for indexes, expr in parse_calc(txt):
        start, end = indexes

        if txt[start - 1] == '(':
            txt = txt[:start] + str(evaluate(*expr)) + txt[end:]
            yield from main(txt)

    # for start, end, n in parse_brackets(txt):
        # txt = txt[:start] + n + txt[end:]
        #yield from main(txt)


    yield txt

if __name__ == "__main__":
    print(list(main('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))[3])