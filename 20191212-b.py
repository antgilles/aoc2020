#!/usr/bin/python

from aocd.models import Puzzle
import re
import ppcm

def parsedata(data):
    p = re.compile('<x=(.*), y=(.*), z=(.*)>')
    dataallaxis=[[] for i in range(3)]
    for line in data.split('\n'):
        res = p.search(line)
        for axis in range(3):
            dataallaxis[axis].append([int(res.group(axis +1)),0])
    return dataallaxis

def getgravity(dataaxis):
    for moon in dataaxis:
        gravity = 0
        for mooncomp in dataaxis:
            if moon[0] < mooncomp[0]:
                gravity += 1
            if moon[0] > mooncomp[0]:
                gravity -= 1
        moon[1] += gravity
    return

def applyvelocity(dataaxis):
    for moon in dataaxis:
            moon[0] += moon[1]
    return

def step(dataaxis):
    getgravity(dataaxis)
    applyvelocity(dataaxis)

def findfrequency(dataaxis):
    count=0
    while True:
        step(dataaxis)
        count += 1
        if dataaxis[0][1] == 0 and dataaxis[1][1] == 0 and dataaxis[2][1] == 0 and dataaxis[3][1] == 0:
            print(count)
            return count


def main():
    puzzle = Puzzle(year=2019, day=12)
    data = puzzle.input_data
    dataallaxis = parsedata(data)
    print(ppcm.ppcm(ppcm.ppcm(findfrequency(dataallaxis[0])*2,findfrequency(dataallaxis[1])*2),findfrequency(dataallaxis[2])*2))

if __name__ == "__main__":
    # execute only if run as a script
    main()
