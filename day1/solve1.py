from itertools import combinations

def num_getter(path):
    with open(path) as l:
        yield from map(int, l)


def part1(nums, target):
    small_chunk = (i for i in nums if 0 < i < 1010)
    big_chunk = {i for i in nums if 1010 < i < 2020}

    for i in small_chunk:
        if (j := target - i) in big_chunk:
            return f'{i} + {j} == {target}\n{i} * {j} == {i * j}' 
 

def part2(nums, target):
    for i, j, k in combinations(nums, 3):
        if i + j + k == 2020:
            return f'{i} + {j} + {k} == 2020\n{i} * {j} * {k} == {i * j * k}'


if __name__ == "__main__":
    nums = set(num_getter('inp.txt'))
    print(part1(nums, 2020), end = 2 * '\n') #p1
    print(part2(nums, 2020)) #p2