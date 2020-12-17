from aocd.models import Puzzle

def getdata(lines):

    z=0
    space={z:{}}
    for y in range(len(lines)):
        space[z][y]={}
        for x in range(len(lines[0])):
            space[z][y][x]=lines[y][x]
    return space

def nbactive(space, x,y,z):
    nb = 0
    for tz in range(-1,2):
        if z + tz in space:
            for ty in range(-1,2):
                if y + ty in space[z + tz]:
                    for tx  in range(-1,2):
                        if x + tx in space[z + tz][y + ty]:
                            if (tx != 0 or ty != 0 or tz != 0) and space[z + tz][y + ty][x + tx] == '#':
                                nb += 1
    return nb

def step(space, count):
    new = {}
    for z in range(-count, count +1):
        for y in range(-count, count +9):
            for x in range(-count, count +9):
                nb = nbactive(space, x,y,z)
                if z in space and y in space[z] and x in space[z][y]:
                    if space[z][y][x] == '#':
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
                if z not in new:
                    new[z]={}
                if y not in new[z]:
                    new[z][y]={}
                new[z][y][x]=state
    return  new

def count(space):
    res = 0
    for z, listy in space.items():
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