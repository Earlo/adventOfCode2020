"""
Advent of Code Challenge 6
"""
import os

dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, 'input'), 'r+') as file:
    lines = [line.strip() for line in file.readlines()]

def part1(answers):
    """Solve Part 1"""
    groups = [set()]
    total = 0
    for line in answers:
        if line == "":
            total += len(groups[-1])
            groups.append(set())
        else:
            groups[-1] = groups[-1].union(set([char for char in line]))
    total += len(groups[-1])
    print(f'{total} in part 1')
    return groups

def part2(answers):
    """Solve Part 2"""
    groups = [set()]
    total = 0
    first = True
    for line in answers:
        if line == "":
            first = True
            total += len(groups[-1])
        else:
            if first:
                first = False
                groups.append(set([char for char in line]))
            else:
                groups[-1].intersection_update(set([char for char in line]))
    total += len(groups[-1])
    print(f'{total} in part 2')
    return groups

if __name__ == '__main__':
    print('Part 1')
    part1(lines)
    print('Part 2')
    part2(lines)
