#!/usr/bin/python

from aocd.models import Puzzle

def getdata(op, curs, param, data):
    if op[-2 - param] == '0':
        return data[data[curs + param]]
    else:
        return data[curs + param]

def intcode(input, data):
    inputpointer = 0
    curs = 0
    while data[curs] != 99:
        op = f'{data[curs]:04}'
        if op[-1] == '1':
            data[data[curs + 3]] = getdata(op, curs, 1, data) + getdata(op, curs, 2, data)
            curs += 4
        elif op[-1] == '2':
            data[data[curs + 3]] = getdata(op, curs, 1, data) * getdata(op, curs, 2, data)
            curs += 4
        elif op[-1] == '3':
            data[data[curs + 1]] = input[inputpointer]
            inputpointer += 1
            curs += 2
        elif op[-1] == '4':
            output = getdata(op, curs, 1, data)
            curs += 2
        elif op[-1] == '5':
            if getdata(op, curs, 1, data) != 0:
                curs = getdata(op, curs, 2, data)
            else:
                curs += 3
        elif op[-1] == '6':
            if getdata(op, curs, 1, data) == 0:
                curs = getdata(op, curs, 2, data)
            else:
                curs += 3
        elif op[-1] == '7':
            if int(getdata(op, curs, 1, data)) < int(getdata(op, curs, 2, data)):
                data[data[curs + 3]] = 1
            else:
                data[data[curs + 3]] = 0
            curs += 4
        elif op[-1] == '8':
            if int(getdata(op, curs, 1, data)) == int(getdata(op, curs, 2, data)):
                data[data[curs + 3]] = 1
            else:
                data[data[curs + 3]] = 0
            curs += 4
    return output


def main():
    input = [5]
    puzzle = Puzzle(year=2019, day=5)
    data = puzzle.input_data.split(',')
    data = list(map(int, data))
    output = intcode(input, data)
    print(output)


if __name__ == "__main__":
    # execute only if run as a script
    main()
