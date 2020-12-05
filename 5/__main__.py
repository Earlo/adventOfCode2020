"""
Advent of Code Challenge 5
"""
import os

dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, 'input'), 'r+') as file:
    lines = [line.strip() for line in file.readlines()]

def getRow(code):
    binary = code.replace('F', '0').replace('B', '1')
    return int(binary, 2)

def getSeat(code):
    binary = code.replace('L', '0').replace('R', '1')
    return int(binary, 2)

def part1(codes):
    """Solve Part 1"""
    highest = 0
    for code in codes:
        row = getRow(code[:-3])
        seat = getSeat(code[-3:])
        highest = max( highest, (row * 8 + seat))
    print(f'{highest} in part 1')
    return highest

def part2(codes):
    """Solve Part 2"""
    seats = [*range(100, 861 + 1)]
    for code in codes:
        row = getRow(code[:-3])
        seat = getSeat(code[-3:])
        print(row * 8 + seat)
        seats.remove(row * 8 + seat)
    print(f'{seats} in part 2')
    return seats

if __name__ == '__main__':
    print('Part 1')
    part1(lines)
    print('Part 2')
    part2(lines)
