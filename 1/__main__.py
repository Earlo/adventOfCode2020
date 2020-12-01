"""
Advent of Code Challenge 1
"""

import os
dirname = os.path.dirname(__file__)

with open(os.path.join(dirname, 'input'), 'r+') as file:
    lines = [int(x) for x in file.readlines()]
    lines.sort()

for ai, a in enumerate(lines):
    for b in lines[:ai]:
        if a + b == 2020:
            print('Part 1')
            print(f'{a} * {b} = {a * b}')


for ai, a in enumerate(lines):
    for bi, b in enumerate(lines[:ai]):
        for c in lines[:bi]:
            if a + b + c == 2020:
                print('Part 2')
                print(f'{a} * {b} * {c} = {a * b * c}')
