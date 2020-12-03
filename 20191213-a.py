#!/usr/bin/python

from aocd.models import Puzzle
import threading, queue

input = queue.Queue()
output = queue.Queue()
resultq = queue.Queue()


def getdata(op, curs, param, base, data):
    if op[-2 - param] == '0':
        return data[data[curs + param]]
    elif op[-2 - param] == '1':
        return data[curs + param]
    else:
        return data[data[curs + param] + base]

def intcode(data, nbwait):
    curs = 0
    base = 0
    nboutput = 0

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
                data[data[curs + 1] + base] = input.get()
            else:
                data[data[curs + 1]] = input.get()
            curs += 2
        elif op[-1] == '4':
            output.put(getdata(op, curs, 1, base, data))
            #print(getdata(op, curs, 1, base, data))
            curs += 2
            nboutput = (nboutput + 1) % 2

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
    output.put(-1)
    return

def robot():
    curdir = 0
    curpos = (0,0)
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    painted = [(0,0)]
    paintedonce = []
    result = 0
    while True:
        if curpos in painted:
            input.put(1)
        else:
            input.put(0)

        paintornot = output.get()
        if paintornot == -1:
            resultq.put(painted)
            return
        if paintornot == 1 and curpos not in paintedonce:
            paintedonce.append(curpos)
            result += 1
        if paintornot == 1 and curpos not in painted:
            painted.append(curpos)
        if paintornot == 0 and curpos in painted:
            painted.remove(curpos)
        newdir = output.get()
        if newdir == 0:
            curdir = (curdir - 1) % 4
        else:
            curdir = (curdir + 1) % 4
        curpos = (curpos[0] + direction[curdir][0], curpos[1] + direction[curdir][1])



def main():


    puzzle = Puzzle(year=2019, day=13)
    data = puzzle.input_data.split(',')
    data = list(map(int, data))
    data += [0]*2048
    t1 = threading.Thread(target=intcode, args=(list(data), 0))
    #t2 = threading.Thread(target=robot, args=())
    t1.start()
    #t2.start()
    t1.join()
    count = 0
    result = 0
    while not output.empty():
        out = output.get()
        if count % 3 == 2 and out == 2:
            result += 1
        count += 1
    print(result)

if __name__ == "__main__":
    # execute only if run as a script
    main()
