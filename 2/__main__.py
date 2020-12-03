"""
Advent of Code Challenge 1
"""
import os

dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, 'input'), 'r+') as file:
    lines = [[
        {
            'min': int(x[0].split('-')[0]),
            'max': int(x[0].split('-')[1]),
            'letter': x[1][0],
            'password': x[2]
        } for x in [line.strip().split(' ')]][0] for line in file.readlines()
    ]

def part1():
    """Solve Part 1"""
    total = 0
    for line in lines:
        if line['max'] >= line['password'].count(line['letter']) >= line['min']:
            total += 1
    print(f'{total} in total at part 1')
    return total

def part2():
    """Solve Part 2"""
    total = 0
    for line in lines:
        minTrue = line['password'][line['min'] - 1] == line['letter']
        maxTrue = line['password'][line['max'] - 1] == line['letter']
        if maxTrue != minTrue:
            total += 1
    print(f'{total} in total at part 2')
    return total

if __name__ == '__main__':
    print('Part 1')
    part1()
    print('Part 2')
    part2()
