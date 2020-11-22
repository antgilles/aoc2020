#!/usr/bin/python


from aocd.models import Puzzle
import collections

def slope_intercept(x1,y1,x2,y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return a

def main():

    puzzle = Puzzle(year=2019, day=10)
    data = puzzle.input_data.split('\n')
    print(data)
    asteroids=[]
    result = 0

    for y in range(len(data)):
        for x in range(len(data[y])):
            print(data[y][x],end='')
            if data[y][x] == '#':
                asteroids.append((x,y))
        print()

    print(asteroids)
    x1 = 28
    y1 = 29

    dicolines=[{},{},{},{}]
    for x2, y2 in asteroids:
        if x1 != x2 or y1 != y2:
            if x1 == x2:
                if y2 > y1:
                    dicoindex = 2
                    a = 0.0
                else:
                    dicoindex = 0
                    a = 0.0
            else:
                if x2 > x1:
                    dicoindex = 1
                else:
                    dicoindex = 3
                a = slope_intercept(x1,y1,x2,y2)
            if a not in dicolines[dicoindex]:
                dicolines[dicoindex][a]=[(x2,y2)]
            else:
                dicolines[dicoindex][a].append((x2,y2))
    print(dicolines)
    odicolines=[]
    for i in dicolines:
        odicolines.append(collections.OrderedDict(sorted(i.items())))
    print(odicolines)
    count = 0
    left = len(asteroids)
    while left > 0:
        for quarter in range(4):
            for dicocoefs in odicolines[quarter].values():
                if len(dicocoefs) > 0:
                    min = abs(dicocoefs[0][0] - x1) + abs(dicocoefs[0][1] - y1)
                    print(dicocoefs)
                    print(min)
                    for x2,y2 in dicocoefs:
                        print(x2,y2, abs(x2 - x1) + abs(y2 - y1))
                        if abs(x2 - x1) + abs(y2 - y1) <= min:
                            min = abs(x2 - x1) + abs(y2 - y1)
                            desintegrated = (x2,y2)
                    print('déinstégré : %s,%s' % desintegrated)
                    dicocoefs.remove(desintegrated)
                    left -= 1
                    count += 1
                    if count == 200:
                        exit(0)
                    print(dicocoefs)
                    print(count)
                    print("-----------")



if __name__ == "__main__":
    # execute only if run as a script
    main()
