#!/usr/bin/python
import math
from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=1)
total_fuel = 0
data = puzzle.input_data.split('\n')

def calc_fuelneed(mass):
    fuel = math.floor((mass) / 3) - 2
    return fuel

for mass in data:
    left_mass = int(mass)
    while left_mass >= 0:
        #print(left_mass)
        left_mass = calc_fuelneed(left_mass)
        if left_mass > 0:
            total_fuel += left_mass

print(str(total_fuel))
#puzzle.answer_b(str(total_fuel))
