import re
from itertools import chain

def get_passports(psfile='inp2.text'):
    passport = ''

    with open(psfile) as lines:
        for line in chain(lines, '\n'):
            if passport and line == '\n': 
                    yield dict(re.findall(r'(\w+):((?:\w|#)+)', passport)) #yielding formatted passport as a dict
                    passport = ''

            else: passport += line.strip() + ' '  


def has_required_fields(passport: dict):
    rf = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} # required fields
    field_set = lambda dic: set( dic.keys() ) - {'cid'}
    
    return rf == field_set(passport)


def p1valids(passports = get_passports):
    return sum( has_required_fields(passport) for passport in passports() )


def p2valids(passports = get_passports):
    # hgt helpers
    unit = lambda l: ''.join( re.findall(r'\D', l) ) # cm or in
    num = lambda l: int( ''.join( re.findall(r'\d', l) ) )

    condition = { 'cm': lambda n: 150 <= n <= 193, 'in': lambda n: 59 <= n <=  76 }
    valid_hgt = lambda x: bool( num(x) ) and ( x.endswith('in') or x.endswith('cm') ) 

    # hcl helper
    hcl_pattern = re.compile( "^#[A-Fa-f0-9]{6}" )

    #pid helper
    pid_pattern = re.compile( "[0-9]{9}" )

    valid_field = {
        'byr': lambda byr: 1920 <= int(byr) <= 2002,
        'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
        'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
        'hgt': lambda hgt: valid_hgt(hgt) and condition[ unit(hgt) ]( num(hgt) ) ,
        'hcl': lambda hcl: bool( re.fullmatch( hcl_pattern, hcl ) ),
        'ecl': lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda pid: bool( re.fullmatch(pid_pattern, pid) )
    }

    def valids():
        for passport in passports():
            if has_required_fields(passport):
                yield all( valid_field[k](v) for k, v in passport.items() if k != 'cid')
    
    return sum( valids() )


if __name__ == "__main__":
    #part 1
    print(p1valids() , '--> part -1 valids' )

    #part 2
    print(p2valids() , '--> part-2 valids' )