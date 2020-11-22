#!/usr/bin/python

from aocd.models import Puzzle

def addinpointdict(dict, point, step):
    if point[0] not in dict:
        dict[point[0]] = {point[1]: step}
    elif point[1] not in dict[point[0]]:
        dict[point[0]][point[1]] = step
    return point


def circuit(wire):
    point = {}
    cur = [0,0]
    step = 0
    for way in wire:
        waydir = way[0]
        waynum = int(way[1:])
        print(waydir,waynum)
        if waydir == "U":
            for count in range(waynum):
                cur[1] += 1
                step += 1
                addinpointdict(point, cur, step)
        elif waydir == "D":
            for count in range(waynum):
                cur[1] -= 1
                step += 1
                addinpointdict(point, cur, step)
        elif waydir == "L":
            for count in range(waynum):
                cur[0] -= 1
                step += 1
                addinpointdict(point, cur, step)
        elif waydir == "R":
            for count in range(waynum):
                cur[0] += 1
                step += 1
                addinpointdict(point, cur, step)
    return point

def main():
    puzzle = Puzzle(year=2019, day=3)
    data = puzzle.input_data.split('\n')
    #data = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83".split('\n')
    #data = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
    wireA = data[0].split(',')
    wireB = data[1].split(',')
    crossed = []
    pointA = circuit(wireA)
    print(pointA)
    pointB = circuit(wireB)
    print(pointB)
    print("circuits ok")
    for x, listy in pointA.items():
        for y, stepA in listy.items():
            if x in pointB and y in pointB[x]:
                crossed.append((x,y, stepA + pointB[x][y]))
    print(crossed)
    result = crossed[0][2]
    for point in crossed:
        if point[2] < result:
            result = point[2]
    print(result)

if __name__ == "__main__":
    # execute only if run as a script
    main()
