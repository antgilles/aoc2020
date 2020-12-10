#!/usr/bin/python

from aocd.models import Puzzle
from collections import Counter



def findnextjolt(lines, previous, visited= None, res = None):
    if visited == None:
        visited = []
        res = []
    candidate = [4,0]
    for line in lines:
        if int(line) not in visited:
            diff = int(line) - previous
            if candidate[0] > diff:
                candidate = [diff, int(line)]
    if candidate[0] < 4:
        visited.append(candidate[1])
        print(candidate)
        res.append(candidate[0])
        res = findnextjolt(lines, candidate[1], visited, res)
    return res



def main():
    puzzle = Puzzle(year=2020, day=10)
    lines = puzzle.input_data.split('\n')

    res = findnextjolt(lines,0)
    print(Counter(res))
    print(Counter(res)[1]*(Counter(res)[3] + 1))



if __name__ == "__main__":
    # execute only if run as a script
    main()


