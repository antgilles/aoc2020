#!/usr/bin/python

from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=5)
result = 0

lines = puzzle.input_data.split('\n')
#lines = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
print(lines)

def dichorow(index, char, min):
    if char == 'F':
        min = min
    else:
        min = min + 128 / pow(2,index)

    return int(min)

def dichocol(index, char, min):
    if char == 'L':
        min = min
    else:
        min = min + 8 / pow(2,index)
    return int(min)

def main():
    puzzle = Puzzle(year=2020, day=5)
    result = 0

    lines = puzzle.input_data.split('\n')
    for line in lines:
        index = 1
        minrow = 0
        for letter in line[:-3]:
            minrow = dichorow(index,letter,minrow)
            index += 1
        index = 1
        mincol = 0
        for letter in line[-3:]:
            mincol = dichocol(index,letter,mincol)
            index += 1
        tmp = (minrow * 8) + mincol
        if result < tmp:
            result = tmp
    print(result)


if __name__ == "__main__":
    # execute only if run as a script
    main()


