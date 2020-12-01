"""
Advent of Code Challenge 1
"""
import os

dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, 'input'), 'r+') as file:
    lines = [int(x) for x in file.readlines()]
    lines.sort()

def part1():
    """Solve Part 1"""
    for aIndex, a in enumerate(lines):
        for b in lines[:aIndex]:
            if a + b == 2020:
                print('Part 1')
                print(f'{a} * {b} = {a * b}')
                return a * b
    return - 1

def part2():
    """Solve Part 2"""
    for aIndex, a in enumerate(lines):
        for bIndex, b in enumerate(lines[:aIndex]):
            for c in lines[:bIndex]:
                if a + b + c == 2020:
                    print('Part 2')
                    print(f'{a} * {b} * {c} = {a * b * c}')
                    return a * b * c
    return -1

if __name__ == '__main__':
    part1()
    part2()
