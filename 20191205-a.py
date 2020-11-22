#!/usr/bin/python

from aocd.models import Puzzle

def getdata(op, curs, param, data):
    if op[-2 - param] == '0':
        return data[data[curs + param]]
    else:
        return data[curs + param]

def main():
    input = 1
    output = []
    puzzle = Puzzle(year=2019, day=5)
    data = puzzle.input_data.split(',')
    #data = ['1','9','10','3','2','3','11','0','99','30','40','50']
    data = list(map(int, data))
    #data[1] = 12
    #data[2] = 2
    curs = 0
    #print(data)
    while data[curs] != 99:
        op = f'{data[curs]:04}'
        #print(op)
        if op[-1] == '1':
            data[data[curs + 3]] = getdata(op, curs, 1, data) + getdata(op, curs, 2, data)
            curs += 4
        elif op[-1] == '2':
            data[data[curs + 3]] = getdata(op, curs, 1, data) * getdata(op, curs, 2, data)
            curs += 4
        elif op[-1] == '3':
            data[data[curs + 1]] = input
            curs += 2
        elif op[-1] == '4':
            output = data[data[curs + 1]]
            curs += 2
        #print(data)


    print(output)
    #puzzle.answer_a(data[0])


if __name__ == "__main__":
    # execute only if run as a script
    main()
