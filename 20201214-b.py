#!/usr/bin/python

from aocd.models import Puzzle

def getalladdress(memaddress, alladdresses, index = 0, prefix=''):
    if index != len(memaddress):
        if memaddress[index] != 'X':
            prefix += memaddress[index]
            index += 1
            getalladdress(memaddress, alladdresses, index, prefix)
        else:
            index += 1
            getalladdress(memaddress, alladdresses, index, prefix + '1')
            getalladdress(memaddress, alladdresses, index, prefix + '0')
    else:
        alladdresses.append(prefix)
        return list(alladdresses)

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
            memaddress = '{:036b}'.format(int(name[4:-1]))
            print(memaddress)
            newmemaddress = []
            for pnt in range(-1,-37, -1 ):
                if mask[pnt] == '0':
                    newmemaddress.insert(0,memaddress[pnt])
                else:
                    newmemaddress.insert(0,mask[pnt])

            print(newmemaddress)
            alladdresses = []
            getalladdress(newmemaddress,alladdresses)
            print(alladdresses)
            for memaddress in alladdresses:
                mem[memaddress]=int(value)
    res = 0
    for key, value in mem.items():
        res += value
    print(res)




if __name__ == "__main__":
    # execute only if run as a script
    main()


