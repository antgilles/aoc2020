#!/usr/bin/python

from aocd.models import Puzzle
import re

def parsedata(data):
    p = re.compile('<x=(.*), y=(.*), z=(.*)>')
    moons=[]
    for line in data.split('\n'):
        res = p.search(line)
        moons.append([[int(res.group(1)),int(res.group(2)),int(res.group(3))],[0,0,0]])
    return

def getgravity(moon, moons, axis)

def getallgravity(moons):
    for axis in range(3):
        for moon in moons:
            moon[1][axis] =

def main():
    puzzle = Puzzle(year=2019, day=12)
    data = puzzle.input_data
    moons = parsedata(data)
    print(moons)


if __name__ == "__main__":
    # execute only if run as a script
    main()
