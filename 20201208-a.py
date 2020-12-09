#!/usr/bin/python

from aocd.models import Puzzle


def apply(inst, arg, res):
    print(inst, arg, res)
    if inst == 'acc':
        res[0] += arg
        res[1] += 1
    elif inst == "jmp":
        res[1] += arg
    elif inst == "nop":
        res[1] += 1
    return res

def gameloop(instlist):
    res = [0,0, []]
    while res[1] < len(instlist):
        print(res)
        operation, arg = instlist[res[1]].split(' ')
        res = apply(operation, int(arg), res)
        if res[1] in res[2]:
            return res
        else:
            res[2].append(res[1])

def main():
    puzzle = Puzzle(year=2020, day=8)
    lines = puzzle.input_data.split('\n')
    res = gameloop(lines)
    print(res[0])


if __name__ == "__main__":
    # execute only if run as a script
    main()


