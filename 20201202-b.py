#!/usr/bin/python
import math
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=2)
result = 0
for line in puzzle.input_data.split('\n'):
    print(line)
    numbersandletter, password = line.split(": ")
    numbers = numbersandletter.split(' ')[0]
    spec = numbersandletter.split(' ')[1]
    flag = 0
    for pos in numbers.split('-'):
        if password[int(pos) - 1] == spec:
            flag += 1
    if flag == 1:
        result += 1

print(result)

#puzzle.answer_a(str(total_fuel))
