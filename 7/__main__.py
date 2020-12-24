"""
Advent of Code Challenge 7
"""
from collections import Counter
import os

dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, 'input'), 'r+') as file:
    lines = [line.strip() for line in file.readlines()]

def buildDictionary(lines):
    d = {}
    for l in lines:
        key, rest = [x.strip() for x in l.replace('.', '').replace('bags', 'bag').split('contain')]
        values = [x.strip() for x in rest.split(',')]
        d[key] = []
        for v in values:
            amount, name = v.split(' ', 1)
            if amount != 'no':
                d[key].append([name, int(amount)])
    return d

def flatBag(bagDict):
    fb = {}
    def flatten(bag, times, debug=False):
        contents = Counter()
        for innerBag, amount in bagDict[bag]:
            if innerBag in contents:
                contents[innerBag] += amount * times
            else:
                contents[innerBag] = amount * times
            innerContents = flatten(innerBag, amount * times)
            contents += innerContents
        return contents
    for bag in bagDict:
        fb[bag] = flatten(bag, 1)
    return fb


def part1(bags):
    """Solve Part 1"""
    target = 'shiny gold bag'
    total = 0
    for b in bags:
        if target in bags[b]:
            total += 1
    print(f'{total} in part 1')
    return total

def part2(bags):
    """Solve Part 2"""
    target = 'shiny gold bag'
    total = 0
    print(bags[target])
    for v in bags[target].values():
        total += v
    print(f'{total} in part 2')
    return total

if __name__ == '__main__':
    flatbags = flatBag(buildDictionary(lines))
    print('Part 1')
    part1(flatbags)
    print('Part 2')
    part2(flatbags)