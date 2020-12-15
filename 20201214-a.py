#!/usr/bin/python

from aocd.models import Puzzle


def main():
    puzzle = Puzzle(year=2020, day=14)
    lines = puzzle.input_data.split('\n')
    mem ={}
    print(lines)

    for line in lines:
        print(line)
        name, value = line.split(' = ')
        if name == 'mask':
            mask = value
        else:
            value = '{:036b}'.format(int(value))
            print(value)
            new = []
            for pnt in range(-1,-37, -1 ):
                if mask[pnt] == 'X':
                    new.insert(0,value[pnt])
                else:
                    new.insert(0,mask[pnt])
            new = int(''.join(new),2)
            print(new)
            mem[name]=new
    res = 0
    for key, value in mem.items():
        res += value
    print(res)




if __name__ == "__main__":
    # execute only if run as a script
    main()


