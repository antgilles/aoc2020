#!/usr/bin/python

from aocd.models import Puzzle

def main():
    puzzle = Puzzle(year=2019, day=4)
    data = puzzle.input_data.split('-')
    result = 0
    for code in range(int(data[0]), int(data[1])+1):
#    for code in [111111, 223450, 123789]:
        code = str(code)
        double = False
        decrease = False
        for num in range(6):
            if num != 0:
                if code[num - 1] > code[num]:
                    decrease = True
                    break
                elif code[num - 1] == code[num]:
                    double = True
        if double is True and decrease is False:
            result += 1
    print(result)

if __name__ == "__main__":
    # execute only if run as a script
    main()
