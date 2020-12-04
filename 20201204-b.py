#!/usr/bin/python
import re
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=4)
result = 0

lines = puzzle.input_data.split('\n')
print(lines)
count = 0


fieldict =  {'ecl':0, 'pid':0, 'eyr':0, 'hcl':0, 'byr':0, 'iyr':0, 'hgt':0}
for line in lines:
    count += 1
    if len(line) == 0 or count > len(lines):
        invalid = 0
        for fieldname, nbfield in fieldict.items():
            if nbfield == 0:
                print('invalid')
                invalid = 1
                break
        if invalid != 1:
            print('valid')
            result += 1
        fieldict = {'ecl':0, 'pid':0, 'eyr':0, 'hcl':0, 'byr':0, 'iyr':0, 'hgt':0}
    else:
        fields = line.split(' ')
        #print(fields)
        for field in fields:
            name,value = field.split(':')
            if name in fieldict:
                if name == 'byr':
                    if int(value) >= 1920 and  int(value) <= 2002:
                        fieldict[name] += 1
                        print('%s : %s valid' % (name, value))
                    else:
                        print('%s : %s INVALID' % (name, value))
                if name == 'iyr':
                    if int(value) >= 2010 and  int(value) <= 2020:
                        fieldict[name] += 1
                        print('%s : %s valid' % (name, value))
                    else:
                        print('%s : %s INVALID' % (name, value))
                if name == 'eyr':
                    if int(value) >= 2020 and  int(value) <= 2030:
                        fieldict[name] += 1
                        print('%s : %s valid' % (name, value))
                    else:
                        print('%s : %s INVALID' % (name, value))
                if name == 'hgt':
                    if value[-2:]== 'in':
                        if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                            fieldict[name] += 1
                            print('%s : %s valid' % (name, value))
                        else:
                            print('%s : %s INVALID' % (name, value))
                    elif value[-2:]== 'cm':
                        if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                            fieldict[name] += 1
                            print('%s : %s valid' % (name, value))
                        else:
                            print('%s : %s INVALID' % (name, value))
                    else:
                        print('%s : %s INVALID' % (name, value))
                if name == 'hcl':
                    m = re.match(r"^#[0-9a-f]{6}$",value)
                    if m:
                        fieldict[name] += 1
                        print('%s : %s valid' % (name, value))
                    else:
                        print('%s : %s INVALID' % (name, value))
                if name == 'ecl':
                    m = re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$",value)
                    if m:
                        print('%s : %s valid' % (name, value))
                        fieldict[name] += 1
                    else:
                        print('%s : %s INVALID' % (name, value))
                if name == 'pid':
                    m = re.match(r"^[0-9]{9}$",value)
                    if m:
                        print('%s : %s valid' % (name, value))
                        fieldict[name] += 1
                    else:
                        print('%s : %s INVALID' % (name, value))
                #print(fieldict)
            #print(name,value)
    if count >= len(lines):
        invalid = 0
        for fieldname, nbfield in fieldict.items():
            if nbfield == 0:
                print('invalid')
                invalid = 1
                break
        if invalid != 1:
            print('valid')
            result += 1
        fieldict = {'ecl':0, 'pid':0, 'eyr':0, 'hcl':0, 'byr':0, 'iyr':0, 'hgt':0}

print(result)


