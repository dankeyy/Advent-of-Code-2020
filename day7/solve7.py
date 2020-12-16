import re
from collections import defaultdict

contained = defaultdict(set)
contains = defaultdict(list)

with open ('inp.txt') as lines:
    for line in lines:
        outercolor = re.match(r'(.+?) bags contain', line)[1]

        for n, innercolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            n = int(n) #how many bags can fit inside another
            contained[innercolor].add(outercolor)
            contains[outercolor].append((n, innercolor))

gold_digger = set() 

def check(color):
    for c in contained[color]:
        gold_digger.add(c)
        check(c)

check('shiny gold')
print( len(gold_digger), '--> p1 sum')

def cost(color):
    summy = 0
    for n, innercolor in contains[color]:
        summy += n
        summy += n * cost(innercolor)
    return summy

print(cost('shiny gold'), '--> p2 sum')