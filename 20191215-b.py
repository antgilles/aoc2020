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

def intcode(data):
    curs = 0
    base = 0
    nboutput = 0
    bufferout = []

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
            #print("INTCODE waitinput")
            output.put(bufferout)
            bufferout = []
            if op[-3] == '2':
                data[data[curs + 1] + base] = input.get()
            else:
                data[data[curs + 1]] = input.get()
            curs += 2
        elif op[-1] == '4':
            print(getdata(op, curs, 1, base, data))
            bufferout.append(getdata(op, curs, 1, base, data))
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
    screen = [ [0]*50 for i in range(25)]
    while True:
        score = 0
        #print('ROBOT - waitoutput')
        data = output.get()
        print(data)
        #printscreen(screen,data)
        boardnew, ball, scorenew = processoutput(data)
        if boardnew:
            board = boardnew
        if scorenew:
            score = scorenew
        if ball < board:
            input.put(-1)
        elif ball > board:
            input.put(1)
        else:
            input.put(0)
        #print(board, ball, score)
        #print(score)




def processoutput(data):
    score = None
    board = None

    for curs in range(0,len(data),3):
        #print(data[curs], data[curs+1], data[curs+2])
        if data[curs] == -1:
            score = data[curs +2]
        if data[curs +2] == 3:
            board = data[curs]
        if data[curs +2] == 4:
            ball = data[curs]
    return board, ball, score

def printscreen(screen, data):
    trans = {0: " ",1: "#", 2: "B", 3: "-", 4: "0"}
    for curs in range(0,len(data),3):
        if data[curs] == -1:
            score = data[curs +2]
        else:
            #print(curs)
            screen[data[curs+1]][data[curs]] = data[curs +2]
            #print(screen)
    for y in range(len(screen)):
        print()
        for x in range(len(screen[y])):
            print(trans[screen[y][x]],end='')
    return

def main():


    puzzle = Puzzle(year=2019, day=13)
    data = puzzle.input_data.split(',')
    data = list(map(int, data))
    data += [0]*2048
    #t1 = threading.Thread(target=intcode, args=(list(data),))

    #t1.start()
    #t1.join()
    data[0]=2
    t1 = threading.Thread(target=intcode, args=(list(data),))
    t2 = threading.Thread(target=robot, args=())
    t1.start()
    t2.start()
    t2.join()



if __name__ == "__main__":
    # execute only if run as a script
    main()
