#!/usr/bin/python
import math
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=2)
result = 0
for line in puzzle.input_data.split('\n'):
    print(line)
    numbersandletter, password = line.split(": ")
    dict = {}
    for letter in password:
        if letter not in dict:
            dict[letter] = 1
        else: dict[letter] += 1
    numbers = numbersandletter.split(' ')[0]
    spec = numbersandletter.split(' ')[1]
    if spec in dict and dict[spec] >= int(numbers.split('-')[0]) and dict[spec] <= int(numbers.split('-')[1]):
        result += 1

    print(result)
#puzzle.answer_a(str(total_fuel))
