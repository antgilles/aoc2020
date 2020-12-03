#!/usr/bin/python
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=3)
lines =  puzzle.input_data.split('\n')

result = 1
for step in [(1, 1), (1, 3), (1, 5), (1, 7)]:
    tree = 0
    xcount = 0
    for y in range(0, len(lines), step[0]):
        if lines[y][xcount % (len(lines[0]))] == '#':
            tree += 1
        xcount += step[1]
    result = result * tree
print(result)

