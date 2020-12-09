#!/usr/bin/python

from aocd.models import Puzzle


def apply(inst, arg, res):
    if inst == 'acc':
        res[0] += arg
        res[1] += 1
    elif inst == "jmp":
        res[1] += arg
    elif inst == "nop":
        res[1] += 1
    return res

def gameloop(instlist):
    res = [0,0, [], -1]
    while res[1] < len(instlist):
        operation, arg = instlist[res[1]].split(' ')
        res = apply(operation, int(arg), res)
        if res[1] in res[2]:
            res[3] = -1
            return res
        else:
            res[2].append(res[1])
            res[3] = 0
    return res

def modify(instlist, index):
    newlist = list(instlist)
    for cur in range(index, len(newlist)):
        if "jmp" in newlist[cur]:
            newlist[cur] = newlist[cur].replace('jmp','nop')
            index +=1
            return(newlist,index)
        elif "nop" in newlist[cur]:
            newlist[cur] = newlist[cur].replace('nop','jmp')
            index +=1
            return(newlist,index)
        index +=1


def main():
    puzzle = Puzzle(year=2020, day=8)
    lines = puzzle.input_data.split('\n')
    res = gameloop(lines)
    index = 0
    while  res[3] != 0:
        newlist, index = modify(lines, index)
        res = gameloop(newlist)
    print(res[0])


if __name__ == "__main__":
    # execute only if run as a script
    main()


