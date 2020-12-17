
def id_getter(bpfile = 'inp.txt'):
    lower = lambda l: l[: len(l) // 2]
    upper = lambda l: l[ len(l) // 2 :]

    narrow = { 'F' : lower, 'B' : upper, 'L' : lower, 'R' : upper } 
    row, column = [ *range(128) ], [ *range(8) ]

    with open (bpfile) as boarding_passes:
        for bp in boarding_passes:                
            bp = bp.strip()
            rbp, cbp = bp[:-3], bp[-3:] # row&column boarding-pass

            seat = {'row': row, 'column': column}

            for letter in rbp: seat['row'] = narrow[letter]( seat['row'] )
            for letter in cbp: seat['column'] = narrow[letter]( seat['column'] )

            yield seat['row'].pop() * 8 + seat['column'].pop() # ID

def p1(ids = id_getter()): 
    return max(ids)

def p2(ids = id_getter()):
    actual_ids = set(ids)
    idrange = set( range( min(actual_ids), max(actual_ids) ) )

    return  (idrange - actual_ids).pop()

if __name__ == "__main__":
    print(p1(), '--> p1 max id value') # part-1
    print(p2(), '--> p2 my id seat') #part-2