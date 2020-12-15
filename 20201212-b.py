#!/usr/bin/python

from aocd.models import Puzzle


def printscreen(lines):
    for y in range(len(lines)):
        print()
        for x in range(len(lines[y])):
            print(lines[y][x], end='')


def forward(pos, facing, value):
    pos = [pos[0] + facing[0] * value, pos[1]+ facing[1] * value]
    return pos

def changefacing(order, facing, degree):
    dir = [[1,0], [0,-1], [-1,0], [0,1]]
    cur = dir.index(facing)
    if order == 'L':
        facing = dir[int((cur - ((degree / 90) % 4) % 4))]
    else:
        facing = dir[int(cur + ((degree / 90) % 4)) % 4]
    return facing

def applyordinal(pos, order, value):
    dir = {'E':[1,0], 'S':[0,-1], 'W':[-1,0], 'N':[0,1]}
    pos = [pos[0] + (dir[order][0]) * value, pos[1] + (dir[order][1] * value)]
    return pos


def looprules(lines):
    pos = [0,0]
    facing = [1,0]
    for line in lines:
        print(line)
        if line[0] == 'F':
            pos = forward(pos, facing, int(line[1:]))
        elif line[0] in ['N','W','S','E']:
            pos = applyordinal(pos, line[0], int(line[1:]))
        else:
            facing = changefacing(line[0], facing, int(line[1:]))
        print(pos, facing)
    return pos

def main():
    puzzle = Puzzle(year=2020, day=12)
    lines = puzzle.input_data.split('\n')

    pos = looprules(lines)
    print(abs(pos[0])+ abs(pos[1]))




if __name__ == "__main__":
    # execute only if run as a script
    main()


