#!/usr/bin/python
import os
from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=2)

noun = -1
verb = 0
result = 0
while result != 19690720:
    if noun == 99:
        if verb == 99:
            print("Not found")
            break
        else:
            verb += 1
            noun = 0
    else:
        noun += 1
    #print("try with noun: %s and verb: %s" % (noun, verb))
    data = puzzle.input_data.split(',')
    data = list(map(int, data))
    data[1] = noun
    data[2] = verb
    curs = 0
    #print(data)

    while data[curs] != 99:
        if data[curs] == 1:
            data[data[curs + 3]] = data[data[curs + 1]] + data[data[curs + 2]]
        elif data[curs] == 2:
            data[data[curs + 3]] = data[data[curs + 1]] * data[data[curs + 2]]
        #print(data)
        curs += 4
    result = data[0]

print("found with noun: %s and verb: %s" % (noun, verb))
print(str(100 * noun + verb))

#puzzle.answer_a(data[0])
