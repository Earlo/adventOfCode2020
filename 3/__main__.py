"""
Advent of Code Challenge 3
"""
import os

dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, 'input'), 'r+') as file:
    lines = [line.strip() for line in file.readlines()]


def testSlope(dx, dy):
    x, y = 0, 0
    total = 0
    width = len(lines[0])
    while y < len(lines):
        if lines[y][x % width] == '#':
            total += 1
        y += dy
        x += dx
    return total



def part1():
    """Solve Part 1"""
    total = testSlope(3, 1)
    print(f'{total} in total at part 1')
    return total

def part2():
    """Solve Part 2"""
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    total = 0
    for slope in slopes:
        if total == 0:
            total += testSlope(*slope)
        else:
            total = total * testSlope(*slope)
    print(f'{total} in total at part 2')
    return total

if __name__ == '__main__':
    print('Part 1')
    part1()
    print('Part 2')
    part2()
