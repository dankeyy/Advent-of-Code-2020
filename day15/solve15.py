from collections import defaultdict, deque
from operator import sub

def getit(starting_numbers, goal):
    keepingscores = defaultdict( lambda: deque(maxlen=2) ) # dict will be constructed as { spoken_number:[deque with 2 recent values] }
    for i, n in enumerate(starting_numbers, 1): keepingscores[n].appendleft(i)
    spoken = starting_numbers[-1]
    start = len(starting_numbers) + 1

    for turn in range(start,  goal+1):
        spoken = 0 if len(keepingscores[spoken]) < 2 else sub(*keepingscores[spoken])
        keepingscores[spoken].appendleft(turn)

    return spoken

if __name__ == "__main__":
    tests = ( [0,3,6], [1,3,2], [2,1,3], [1,2,3], [2,3,1], [3,2,1], [3,1,2] )
    for test in tests:
        print(f'{test}->', getit(test, 2020))

    pazzle_input = [0,3,1,6,7,5]
    print(f'{pazzle_input = } -> ', getit(pazzle_input, 30000000))