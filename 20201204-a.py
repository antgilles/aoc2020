#!/usr/bin/python
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=4)
result = 0

lines = puzzle.input_data.split('\n')
print(lines)
fieldict =  {'ecl':0, 'pid':0, 'eyr':0, 'hcl':0, 'byr':0, 'iyr':0, 'hgt':0}
for line in lines:
    if len(line) == 0:
        invalid = 0
        for fieldname, nbfield in fieldict.items():
            if nbfield == 0:
                print('invalid')
                invalid = 1
                break
        if invalid != 1:
            result += 1
        fieldict = {'ecl':0, 'pid':0, 'eyr':0, 'hcl':0, 'byr':0, 'iyr':0, 'hgt':0}
    else:
        fields = line.split(' ')
        print(fields)
        for field in fields:
            name,value = field.split(':')
            if name in fieldict:
                fieldict[name] += 1
                print(fieldict)
            print(name,value)

print(result)


