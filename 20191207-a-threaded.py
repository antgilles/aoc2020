#!/usr/bin/python

from aocd.models import Puzzle
import threading

output = [0,0,0,0,0]
wait = []
phase = []

def getdata(op, curs, param, data):
    if op[-2 - param] == '0':
        return data[data[curs + param]]
    else:
        return data[curs + param]

def intcode(phase, output, data, index, wait):
    curs = 0
    while data[curs] != 99:
        while wait[index]:
            i =1
        op = f'{data[curs]:04}'
        if op[-1] == '1':
            data[data[curs + 3]] = getdata(op, curs, 1, data) + getdata(op, curs, 2, data)
            curs += 4
        elif op[-1] == '2':
            data[data[curs + 3]] = getdata(op, curs, 1, data) * getdata(op, curs, 2, data)
            curs += 4
        elif op[-1] == '3':
            if phase < 0:
                data[data[curs + 1]] = output[(index - 1) % 5 ]
            else:
                data[data[curs + 1]] = phase
                phase = -1
            curs += 2
        elif op[-1] == '4':
            output[index] = getdata(op, curs, 1, data)
            wait[index] = True
            wait[(index + 1) % 5] = False
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
    return 0


def main():
    puzzle = Puzzle(year=2019, day=7)
    data = puzzle.input_data.split(',')
    #data = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(',')
    data = list(map(int, data))
    result = 0

    for a in range(5):
        for b in range(5):
            if b == a: continue
            for c in range(5):
                if c == a or c == b: continue
                for d in range(5):
                    if d == a or d == b or d == c: continue
                    for e in range(5):
                        if e == a or e == b or e == c or e == d : continue
                        output = [0,0,0,0,0]
                        wait = [False,True,True,True,True]
                        t1 = threading.Thread(target=intcode, args=(a, output, list(data),0,wait))
                        t2 = threading.Thread(target=intcode, args=(b, output, list(data),1,wait))
                        t3 = threading.Thread(target=intcode, args=(c, output, list(data),2,wait))
                        t4 = threading.Thread(target=intcode, args=(d, output, list(data),3,wait))
                        t5 = threading.Thread(target=intcode, args=(e, output, list(data),4,wait))
                        t1.start()
                        t2.start()
                        t3.start()
                        t4.start()
                        t5.start()
                        t5.join()
                        if output[4] > result:
                            result = output[4]


    print(result)

if __name__ == "__main__":
    # execute only if run as a script
    main()
