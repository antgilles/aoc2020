#!/usr/bin/python

from aocd.models import Puzzle

def main():
    puzzle = Puzzle(year=2020, day=6)
    result = 0

    lines = puzzle.input_data.split('\n')
    print(lines)
    grpanswers = []
    nbanswers = 0
    already = {}
    nbpers = 0
    for index in range(len(lines)):
        print(lines[index])
        if len(lines[index]) == 0:
            print(nbpers)
            print(already)
            for alr, value in already.items():
                if value == nbpers:
                    nbanswers += 1
            grpanswers.append(nbanswers)
            nbanswers = 0
            already = {}
            nbpers = 0
        else:
            for answer in lines[index]:
                print(answer)
                if answer not in already:
                    already[answer] = 1
                else:
                    already[answer]+=1
            print(grpanswers)
            nbpers += 1
    for alr, value in already.items():
        if value == nbpers:
            nbanswers += 1
    grpanswers.append(nbanswers)
    print(grpanswers)
    for i in grpanswers:
        result += i


    print(result)


if __name__ == "__main__":
    # execute only if run as a script
    main()

