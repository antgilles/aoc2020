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
            if op[-3] == '2':
                data[data[curs + 1] + base] = input.get()
            else:
                data[data[curs + 1]] = input.get()
            curs += 2
        elif op[-1] == '4':
            #print(getdata(op, curs, 1, base, data))
            output.put(getdata(op, curs, 1, base, data))
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



def robot(pos=(0,0), screen = {'ymin':0, 'ymax':0, 'xmin':0,'xmax':0, 0: {0: 5}}):
    direction = [(0,-1,2),(0,1,1),(-1,0,4),(1,0,3)]
    for dir in range(1,5):
        newpos = (pos[0] + direction[dir - 1][0], pos[1] + direction[dir - 1][1])
        #print(newpos)
        if newpos[0] < screen['xmin']: screen['xmin'] = newpos[0]
        elif newpos[0] > screen['xmax']: screen['xmax'] = newpos[0]
        if newpos[1] < screen['ymin']: screen['ymin'] = newpos[1]
        elif newpos[1] > screen['ymax']: screen['ymax'] = newpos[1]
        if newpos[1] in screen and newpos[0] in screen[newpos[1]]:
            #print("depuis pos %s pour direction %s : already visited" % (pos, dir))
            continue
        input.put(dir)
        data = output.get()
        #print("resultat intcode depuis pos %s pour direction %s : %s" % (pos, dir, data))

        if newpos[1] not in screen:
             screen[newpos[1]]={}
        screen[newpos[1]][newpos[0]] = data
        if data != 0:
            #print("call robot with %s and screen %s" % (newpos,screen))
            robot(newpos, screen)
            input.put(direction[dir - 1][2])
            output.get()
        if data == 2:
            print(newpos)
    if pos == (0,0):
        input.put(0)
        printscreen(screen)

def shortestpath():
    return

def printscreen(screen):
    print('------------------------------------------------------------------')
    trans = {0: "#",1: ".", 2: "B", 3: "-", 4: "0", 5: "S"}
    for y in range(screen['ymin'], screen['ymax'] + 1):
        print()
        for x in range(screen['xmin'],screen['xmax'] + 1):
            if y in screen and x in screen[y]:
                print(trans[screen[y][x]], end='')
            else:
                print('?', end='')
    return

def main():


    puzzle = Puzzle(year=2019, day=15)
    data = puzzle.input_data.split(',')
    data = list(map(int, data))
    data += [0]*2048

    t1 = threading.Thread(target=intcode, args=(list(data),))
    t2 = threading.Thread(target=robot, args=())
    t2.start()
    t1.start()
    t2.join()
    print("end of main")
    exit()

if __name__ == "__main__":
    # execute only if run as a script
    main()
