#!/usr/bin/python

#!/usr/bin/python

from aocd.models import Puzzle

def slope_intercept(x1,y1,x2,y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return a,b

def main():

    puzzle = Puzzle(year=2019, day=10)
    data = puzzle.input_data.split('\n')
    #data = ".#..#\n.....\n#####\n....#\n...##\n".split('\n')
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

    for x1, y1 in asteroids:
        dicolines={}
        for x2, y2 in asteroids:
            if x1 != x2 or y1 != y2:
                if x1 == x2:
                    a = 'inf'
                    b = 'inf'
                else:
                    a, b = slope_intercept(x1,y1,x2,y2)
                if (a,b) not in dicolines:
                    dicolines[(a,b)]=[(x2,y2)]
                else:
                    dicolines[(a,b)].append((x2,y2))
        #print(dicolines)

        seen = 0
        for inlines in dicolines.values():
            min = 0
            max = 0
            for inline in inlines:
                if x1 + y1 < inline[0] + inline[1]:
                    max = 1
                else:
                    min = 1
            seen += min + max
        print(x1, y1 ,seen)
        if seen > result:
            result = seen + 1
            coord = (x1, y1)
    print(result, coord)


if __name__ == "__main__":
    # execute only if run as a script
    main()
