"""
Advent of Code Challenge 7
"""
import os

dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, 'input'), 'r+') as file:
    lines = [line.strip() for line in file.readlines()]

def getCommands(lines):
    d = []
    for l in lines:
        command, value = [x.strip() for x in l.split(' ')]
        d.append([command, int(value)])
    return d

def part1(commands):
    """Solve Part 1"""
    accumulator = 0
    i = 0
    fresh = set(range(len(commands)))
    while i < len(commands):
        if i in fresh:
            fresh.remove(i)
        else:
            #print('repeat at', i)
            break
        print(i, accumulator)
        command, value = commands[i]
        if command == 'jmp':
            i += value
        else:
            if command == 'acc':
                accumulator += value
            i += 1
    print(f'{accumulator} in part 1')
    return accumulator

def part2(commands):
    """Solve Part 2"""
    accumulator = 0
    i = 0
    fresh = set(range(len(commands)))
    jumps = []
    swap = False
    while i < len(commands):
        print(i)
        if i in fresh:
            add = 1
            command, value = commands[i]
            if (command == 'acc'):
                if swap:
                    print('?????')
                accumulator += value
                #print("accumuulated", accumulator)

            elif (command == 'jmp' and not swap) or (command == 'nop' and swap):
                if swap:
                    swap = False
                else:
                    jumps.append([i, fresh.copy(), accumulator])
                add = value
            elif (command == 'nop' and not swap) or (command == 'jmp' and swap):
                if swap:
                    swap = False
                else:
                    jumps.append([i, fresh.copy(), accumulator])
            else:
                print('????')
            fresh.remove(i)
            i+=add

        else:
            print('repeat at', i, len(fresh), accumulator)
            i, fresh, accumulator = jumps.pop()
            swap = True
            print('return to', i, len(fresh), accumulator)

    print(f'{accumulator} in part 2')
    return accumulator

if __name__ == '__main__':
    commands = getCommands(lines)
    print('Part 1')
    part1(commands)
    print('Part 2')
    part2(commands)