#!/usr/bin/python

from aocd.models import Puzzle

def main():
    puzzle = Puzzle(year=2020, day=6)
    result = 0

    lines = puzzle.input_data.split('\n')
    print(lines)
    grpanswers = []
    nbanswers = 0
    already = []
    for index in range(len(lines)):
        print(lines[index])
        if len(lines[index]) == 0:
            grpanswers.append(nbanswers)
            nbanswers = 0
            already = []
        else:
            for answer in lines[index]:
                print(answer)
                if answer not in already:
                    print('ADD')
                    already.append(answer)
                    nbanswers += 1
            print(grpanswers)
    grpanswers.append(nbanswers)
    print(grpanswers)
    for i in grpanswers:
        result += i


    print(result)


if __name__ == "__main__":
    # execute only if run as a script
    main()

