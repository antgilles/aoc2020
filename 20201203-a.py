#!/usr/bin/python
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=3)
result = 0

lines = puzzle.input_data.split('\n')
xcount = 0
tree = 0
for y in range(len(lines)):
    if lines[y][xcount % (len(lines[0]))] == '#':
        tree += 1
    xcount += 3
print(tree)

