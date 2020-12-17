from aocd.models import Puzzle

def getdata(lines):
    z=0
    w=0
    space={w:{z:{}}}
    for y in range(len(lines)):
        space[w][z][y]={}
        for x in range(len(lines[0])):
            space[w][z][y][x]=lines[y][x]
    return space

def nbactive(space, x,y,z,w):
    nb = 0
    for tw in range(-1,2):
        if w + tw in space:
            for tz in range(-1,2):
                if z + tz in space[w + tw]:
                    for ty in range(-1,2):
                        if y + ty in space[w + tw][z + tz]:
                            for tx  in range(-1,2):
                                if x + tx in space[w + tw][z + tz][y + ty]:
                                    if (tw != 0 or tx != 0 or ty != 0 or tz != 0) and space[w + tw][z + tz][y + ty][x + tx] == '#':
                                        nb += 1
    return nb

def step(space, count):
    new = {}
    for w in range(-count, count +1):
        for z in range(-count, count +1):
            for y in range(-count, count +9):
                for x in range(-count, count +9):
                    nb = nbactive(space, x,y,z,w)
                    if w in space and z in space[w] and y in space[w][z] and x in space[w][z][y]:
                        if space[w][z][y][x] == '#':
                            if nb == 3 or nb == 2:
                                state = "#"
                            else:
                                state = "."
                        else:
                            if nb == 3:
                                state = "#"
                            else:
                                state = "."
                    else:
                        if nb == 3:
                            state = "#"
                        else:
                            state = "."
                    if w not in new:
                        new[w]={}
                    if z not in new[w]:
                        new[w][z]={}
                    if y not in new[w][z]:
                        new[w][z][y]={}
                    new[w][z][y][x]=state
    return  new

def count(space):
    res = 0
    for w, listw in space.items():
        for z, listy in listw.items():
            for y, listx in listy.items():
                for x, state in listx.items():
                    if state == '#':
                        res += 1
    print(res)

def loop(space):
    for count in range(1,7):
        space = step(space, count)
    return space

def main():
    puzzle = Puzzle(year=2020, day=17)
    lines = puzzle.input_data.split('\n')
    space = getdata(lines)
    space = loop(space)
    count(space)



if __name__ == "__main__":
    # execute only if run as a script
    main()