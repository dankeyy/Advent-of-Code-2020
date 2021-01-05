import re
from operator import add, mul
from copy import deepcopy

opr = {'+': add, '*': mul}
evaluate = lambda x, n1, n2: opr[x](n1, n2)

def parse_calc(txt):
    for i in re.finditer(r"((\d+) (\W) (\d+)|(\()(\d+)(\)))", txt):
        _, n1, x, n2 = i.groups() # Ns are either braces or numbers
        indexes = i.span()

        if x.isnumeric(): yield indexes, i.string[1:-1]
        else: yield indexes, (x, *map( int, (n1, n2) ) )

def main(txt):
    # clone = deepcopy(txt)
    for indexes, innerexpr in parse_calc(txt):
        start, end = indexes

        if innerexpr.isnumeric():
            txt = txt[:start] + innerexpr + txt[end:]
        else:
            if txt[start - 1] == '(':
                txt = txt[:start] + str(evaluate(*innerexpr)) + txt[end:]
            yield from main(txt)

    # for start, end, n in parse_brackets(txt):
        # txt = txt[:start] + n + txt[end:]
        #yield from main(txt)


    yield txt

if __name__ == "__main__":
    print(list(main('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))[3])