#!/usr/bin/python

from aocd.models import Puzzle


def isnotok(lines, index, preamb):
    for x in range(index - preamb, index):
        for y in range(index - preamb, index):
            if x != y and int(lines[x]) + int(lines[y]) == int(lines[index]):
                return 0
    return 1

def main():
    puzzle = Puzzle(year=2020, day=9)
    preamb = 25
    lines = puzzle.input_data.split('\n')
    for index in range(preamb, len(lines)):
        if isnotok(lines, index, preamb):
            print(lines[index])



if __name__ == "__main__":
    # execute only if run as a script
    main()


