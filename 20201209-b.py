#!/usr/bin/python

from aocd.models import Puzzle


def isnotok(lines, index, preamb):
    for x in range(index - preamb, index):
        for y in range(index - preamb, index):
            if x != y and int(lines[x]) + int(lines[y]) == int(lines[index]):
                return 0
    return 1

def isweakness(lines, index, find):
    test = 0
    testlist = []
    for x in range(index, len(lines)):
        testlist.append(int(lines[x]))
        test += int(lines[x])
        if test == find and len(testlist) > 1:
            return (0,testlist)
    return (1, [])


def main():
    puzzle = Puzzle(year=2020, day=9)
    preamb = 25
    lines = puzzle.input_data.split('\n')
    for index in range(preamb, len(lines)):
        if isnotok(lines, index, preamb):
            find = int(lines[index])

    for index in range(len(lines)):
        res = isweakness(lines,index,find)
        if res[0] == 0:
            print(min(res[1]) + max(res[1]))



if __name__ == "__main__":
    # execute only if run as a script
    main()


