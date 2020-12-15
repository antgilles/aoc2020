#!/usr/bin/python

from aocd.models import Puzzle
import copy

def getdict(lines):
    dict = {}
    for y in range(len(lines)):
        dict[y]={}
        for x in range(len(lines[y])):
            dict[y][x]=lines[y][x]
    return dict

def printscreen(lines):
    for y in range(len(lines)):
        print()
        for x in range(len(lines[y])):
            print(lines[y][x], end='')

def totaloccupied(lines):
    res = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                res += 1
    return res

def nboccupied(lines, seat):
    x, y = seat
    res = 0
    for testx in range(-1,2):
        for testy in range(-1,2):
            if testx != 0 or testy != 0:
                if y + testy >= 0 and y + testy < len(lines) and x + testx >= 0 and x + testx < len(lines[0]) and lines[y + testy][x + testx] == '#':
                    res += 1
    return res

def applyrule(lines):
    new = copy.deepcopy(lines)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            new[y][x] = lines[y][x]
            if lines[y][x] != '.':
                nb = nboccupied(lines, (x,y))
            if lines[y][x] == 'L' and nb == 0:
                new[y][x] = '#'
            elif lines[y][x] == '#' and nb >= 4:
                new[y][x] = 'L'
    return new

def looprules(lines):
    printscreen(lines)
    print()
    while True:
        new = applyrule(lines)
        #print()
        #print('-------------------------')
        #printscreen(lines)
        if lines == new:
           return new
        else:
            lines = new


def main():
    puzzle = Puzzle(year=2020, day=11)
    lines = puzzle.input_data.split('\n')

    lines = getdict(lines)
    print(totaloccupied(looprules(lines)))





if __name__ == "__main__":
    # execute only if run as a script
    main()


