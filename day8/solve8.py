
with open('inp.txt') as f:
    lines = [ l.rstrip('\n') for l in f.readlines() ]


def halt(lines):
    i = acc = 0
    been_here = set()

    while i < len(lines):
        if i in been_here: return #acc # acc if p1, nothing (none) if p2 
        else: been_here.add(i)

        operation, n = lines[i].split() 
        n = int(n)

        if operation == 'jmp': i += n
        else:
            i += 1
            if operation == 'acc': acc += n

    return acc


def halt_fix(lines):
    reverse = {'jmp': 'nop', 'nop': 'jmp'}

    for i in range( len(lines) ) : 
        operation, n = lines[i].split() 

        if operation != 'acc':
            maybe_fixed_line = [f'{reverse[operation]} {n}']
            maybe_fixed_lines = lines[:i] + maybe_fixed_line + lines[i + 1:]
        
            if (acc := halt(maybe_fixed_lines)) != None:
                return acc


if __name__ == "__main__":
    print(halt(lines))
    print(halt_fix(lines))