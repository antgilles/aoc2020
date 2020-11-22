#!/usr/bin/python

from aocd.models import Puzzle
from intcode import intcode



def main():
    puzzle = Puzzle(year=2019, day=7)
    data = puzzle.input_data.split(',')
    #data = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(',')
    data = list(map(int, data))
    result = 0

    for a in range(5):
        outputa = intcode([a,0], data)
        for b in range(5):
            if b == a: continue
            outputb = intcode([b,outputa], data)
            for c in range(5):
                if c == a or c == b: continue
                outputc = intcode([c, outputb], data)
                for d in range(5):
                    if d == a or d == b or d == c: continue
                    outputd = intcode([d, outputc], data)
                    for e in range(5):
                        if e == a or e == b or e == c or e == d : continue
                        outpute = intcode([e, outputd], data)
                        if outpute > result:
                            result = outpute
    print(result)

if __name__ == "__main__":
    # execute only if run as a script
    main()
