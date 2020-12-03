#!/usr/bin/python
import math
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=1)

for i in puzzle.input_data.split('\n'):
    for j in puzzle.input_data.split('\n'):
        if int(i) + int(j) == 2020:
            print(int(i) * int(j))

print()
#puzzle.answer_a(str(total_fuel))
