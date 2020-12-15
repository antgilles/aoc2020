#!/usr/bin/python

from aocd.models import Puzzle

def forward(pos, wpt, value):
    pos = [pos[0] + wpt[0] * value, pos[1]+ wpt[1] * value]
    return pos

def changeangle(order, wpt, degree):
    angle = int((degree / 90) % 4)
    if order == 'L':
        if angle == 1:
            wpt = [-wpt[1], wpt[0]]
        if angle == 2:
            wpt = [-wpt[0], -wpt[1]]
        if angle == 3:
            wpt = [wpt[1], -wpt[0]]
    else:
        if angle == 1:
            wpt = [wpt[1],-wpt[0]]
        if angle == 2:
            wpt = [-wpt[0], -wpt[1]]
        if angle == 3:
            wpt = [-wpt[1], wpt[0]]
    return wpt

def applyordinal(pos, order, value):
    dir = {'E':[1,0], 'S':[0,-1], 'W':[-1,0], 'N':[0,1]}
    pos = [pos[0] + (dir[order][0]) * value, pos[1] + (dir[order][1] * value)]
    return pos


def looprules(lines):
    pos = [0,0]
    wpt = [10,1]
    for line in lines:
        print(line)
        if line[0] == 'F':
            pos = forward(pos, wpt, int(line[1:]))
        elif line[0] in ['N','W','S','E']:
            wpt = applyordinal(wpt, line[0], int(line[1:]))
        else:
            wpt = changeangle(line[0], wpt, int(line[1:]))
        print(pos, wpt)
    return pos

def main():
    puzzle = Puzzle(year=2020, day=12)
    lines = puzzle.input_data.split('\n')

    pos = looprules(lines)
    print(abs(pos[0])+ abs(pos[1]))




if __name__ == "__main__":
    # execute only if run as a script
    main()


