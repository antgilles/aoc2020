#!/usr/bin/python

from aocd.models import Puzzle


def main():
    puzzle = Puzzle(year=2020, day=13)
    lines = puzzle.input_data.split('\n')
    ts = int(lines[0])
    buses = lines[1].split(',')
    res = 10000000
    for bus in buses:
        print(bus)
        if bus != 'x':
            bus = int(bus)
            mod = ts % bus
            print(mod)
            if mod == 0:
                res = 0
                resbus = bus
                break
            else:
                print(bus - mod)
                if bus - mod < res:
                    res = bus - mod
                    resbus = bus
    print(res * resbus)





if __name__ == "__main__":
    # execute only if run as a script
    main()


