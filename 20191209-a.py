#!/usr/bin/python

from aocd.models import Puzzle

def getdata(op, curs, param, base, data):
    if op[-2 - param] == '0':
        return data[data[curs + param]]
    elif op[-2 - param] == '1':
        return data[curs + param]
    else:
        return data[data[curs + param] + base]

def intcode(input, data):
    inputpointer = 0
    curs = 0
    base = 0
    while data[curs] != 99:
        op = f'{data[curs]:05}'
        if op[-1] == '1':
            if op[-5] == '2':
                data[data[curs + 3] + base] = getdata(op, curs, 1, base, data) + getdata(op, curs, 2, base, data)
            else:
                data[data[curs + 3]] = getdata(op, curs, 1, base, data) + getdata(op, curs, 2, base, data)
            curs += 4
        elif op[-1] == '2':
            if op[-5] == '2':
                data[data[curs + 3] + base] = getdata(op, curs, 1, base, data) * getdata(op, curs, 2, base, data)
            else:
                data[data[curs + 3]] = getdata(op, curs, 1, base, data) * getdata(op, curs, 2, base, data)
            curs += 4
        elif op[-1] == '3':
            if op[-3] == '2':
                data[data[curs + 1] + base] = input[inputpointer]
            else:
                data[data[curs + 1]] = input[inputpointer]
            inputpointer += 1
            curs += 2
        elif op[-1] == '4':
            output = getdata(op, curs, 1, base, data)
            curs += 2
            print("ouput: %s" % output)
        elif op[-1] == '5':
            if getdata(op, curs, 1, base, data) != 0:
                curs = getdata(op, curs, 2, base, data)
            else:
                curs += 3
        elif op[-1] == '6':
            if getdata(op, curs, 1, base, data) == 0:
                curs = getdata(op, curs, 2, base, data)
            else:
                curs += 3
        elif op[-1] == '7':
            if op[-5] == '2':
                index = data[curs + 3] + base
            else:
                index = data[curs + 3]
            if int(getdata(op, curs, 1, base, data)) < int(getdata(op, curs, 2, base, data)):
                data[index] = 1
            else:
                data[index] = 0
            curs += 4
        elif op[-1] == '8':
            if op[-5] == '2':
                index = data[curs + 3] + base
            else:
                index = data[curs + 3]
            if int(getdata(op, curs, 1, base, data)) == int(getdata(op, curs, 2, base, data)):
                data[index] = 1
            else:
                data[index] = 0
            curs += 4
        elif op[-1] == '9':
            base += getdata(op, curs, 1, base, data)
            curs += 2
    return output


def main():
    input = [2]
    puzzle = Puzzle(year=2019, day=9)
    data = puzzle.input_data.split(',')
    #data = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(',')
    #data = "104,1125899906842624,99".split(',')
    data = list(map(int, data))
    data += [0]*2048
    output = intcode(input, data)
    print(output)


if __name__ == "__main__":
    # execute only if run as a script
    main()
