#!/usr/bin/python
import math
from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=1)
total_fuel = 0
for mass in puzzle.input_data.split('\n'):
    fuel = math.floor(int(mass) / 3) - 2
    total_fuel += fuel

print(str(total_fuel))
#puzzle.answer_a(str(total_fuel))
