"""
Advent of Code Challenge 4
"""
import os

dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, 'input'), 'r+') as file:
    lines = [line.strip() for line in file.readlines()]

passports = []
keysPart1 = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]
keys = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
]


def getPassports():
    """
    Get Passport data
    """
    passport = {}
    passports.append(passport)
    for l in lines:
        pairs = l.strip().split(' ')
        # print(d)
        if pairs[0] == '':
            print('Add passport', passport)
            passport = {}
            passports.append(passport)
        else:
            print('valid lien')
            try:
                i = 0
                while 1:
                    key, value = pairs[i].split(':')
                    passport[key] = value
                    i += 1
            except Exception as e:
                pass
    return passports


def validate(value, key):
    print(key, value)
    if key == 'byr':
        print( 2002 >= int(value) >= 1920)
        return( 2002 >= int(value) >= 1920)
    elif key == 'iyr':
        print( 2020 >= int(value) >= 2010)
        return( 2020 >= int(value) >= 2010)
    elif key == 'eyr':
        print( 2030 >= int(value) >= 2020)
        return( 2030 >= int(value) >= 2020)
    elif key == 'hgt':
        print( (value[-2:] == 'cm' and 193 >= int(value[:-2]) >= 150) or (value[-2:] == 'in' and 76 >= int(value[:-2]) >= 59))
        return( (value[-2:] == 'cm' and 193 >= int(value[:-2]) >= 150) or (value[-2:] == 'in' and 76 >= int(value[:-2]) >= 59))
    elif key == 'hcl':
        print(value[:1] == '#', value[1:])
        try:
            int(value[1:], 16)
            return (value[:1] == '#')
        except Exception as e:
            pass
    elif key == 'ecl':
        print( value in ['amb','blu','brn','gry','grn','hzl','oth'])
        return( value in ['amb','blu','brn','gry','grn','hzl','oth'])
    elif key == 'pid':
        print( (len(value) == 9) and (int(value)))
        return( (len(value) == 9) and (int(value)))
    elif key == 'cid':
        print( True)

def part1(passports):
    """Solve Part 1"""
    total = 0
    for p in passports:
        if all(key in p for key in keysPart1):
            total += 1
    print(f'{total} in total at part 1')
    return total

def part2(passports):
    """Solve Part 2"""
    total = 0
    for p in passports:
        if all(key in p for key in keysPart1):
            if all(validate(p[key], key) for key in keysPart1):
                total += 1

    print(f'{total} in total at part 2')
    return total

if __name__ == '__main__':
    passports = getPassports()
    print('Part 1')
    part1(passports)
    print('Part 2')
    part2(passports)
