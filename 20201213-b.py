#!/usr/bin/python

from aocd.models import Puzzle

def getdiff(prev, frequency, line, diff ):
    new = prev
    flag=0
    while True:
        if (new + diff) % line == 0:
            print(new)
            flag +=1
            if flag == 2:
                return(min, new - min)
            else:
                min = new
        new += frequency

def main():
    puzzle = Puzzle(year=2020, day=13)
    lines = puzzle.input_data.split('\n')
    ts = int(lines[0])
    buses = lines[1].split(',')
    ref = int(buses.pop(0))
    frequency = ref
    cnt = 0
    for bus in buses:
        print(bus)
        cnt +=1
        if bus != 'x':
            bus = int(bus)
            ref, frequency = getdiff(ref, frequency, bus, cnt)
            print(frequency, ref)

if __name__ == "__main__":
    # execute only if run as a script
    main()


