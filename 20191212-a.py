#!/usr/bin/python

from aocd.models import Puzzle
import re

def parsedata(data):
    p = re.compile('<x=(.*), y=(.*), z=(.*)>')
    moons=[]
    for line in data.split('\n'):
        res = p.search(line)
        moons.append([[int(res.group(1)),int(res.group(2)),int(res.group(3))],[0,0,0]])
    return moons

def getgravity(moon, moons, axis):
    gravity = 0
    for mooncomp in moons:
        if moon[0][axis] < mooncomp[0][axis]:
            gravity += 1
        if moon[0][axis] > mooncomp[0][axis]:
            gravity -= 1
    return gravity

def getallgravity(moons):
    for axis in range(3):
        for moon in moons:
            moon[1][axis] += getgravity(moon,moons,axis)
    return moons

def applyvelocity(moons):
    for axis in range(3):
        for moon in moons:
            moon[0][axis] += moon[1][axis]
    return moons

def step(moons):
    moons = getallgravity(moons)
    moons = applyvelocity(moons)

    return moons

def repeatstep(moons, nbstep):
    for i in range (nbstep):
        moons = step(moons)
    return moons

def calcenergy(moons):
    energy = 0
    for moon in moons:
        energypot = 0
        energykin = 0
        for axis in range(3):
            energypot += abs(moon[0][axis])
            energykin += abs(moon[1][axis])
        energy += energypot * energykin
    return energy

def main():
    puzzle = Puzzle(year=2019, day=12)
    data = puzzle.input_data
    moons = parsedata(data)
    moons = repeatstep(moons,1000)
    print(moons)
    energy = calcenergy(moons)
    print(energy)


if __name__ == "__main__":
    # execute only if run as a script
    main()
