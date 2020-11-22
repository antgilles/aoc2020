#!/usr/bin/python
import os
from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=2)
data = puzzle.input_data.split(',')
#data = ['1','9','10','3','2','3','11','0','99','30','40','50']
data = list(map(int, data))
data[1] = 12
data[2] = 2
curs = 0
#print(data)
while data[curs] != 99:
    if data[curs] == 1:
        data[data[curs + 3]] = data[data[curs + 1]] + data[data[curs + 2]]
    elif data[curs] == 2:
        data[data[curs + 3]] = data[data[curs + 1]] * data[data[curs + 2]]
    #print(data)
    curs += 4

print(data[0])
#puzzle.answer_a(data[0])
