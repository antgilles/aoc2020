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
    dirs = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for dir in dirs:
        x, y = seat
        while x + dir[0] >= 0 and x + dir[0] < len(lines[0]) and y + dir[1] >= 0 and y + dir[1] < len(lines):
            x += dir[0]
            y += dir[1]
            if lines[y][x] == '#':
                res += 1
                break
            if lines[y][x] == 'L':
                break
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
            elif lines[y][x] == '#' and nb >= 5:
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


