#!/usr/bin/python

from aocd.models import Puzzle

def main():
    puzzle = Puzzle(year=2019, day=8)
    data = puzzle.input_data
    #data = "0222112222120000"
    wide = 25
    tall = 6

    layers = [data[i: i + tall * wide] for i in range(0, len(data), tall * wide)]
    output = [0] * tall * wide
    for cursor in range(tall * wide):
        for layer in layers:
            if layer[cursor] != "2":
                output[cursor] = (layer[cursor])
                break

    for x in range(len(output)):
        if x % wide == 0:
            print("")
        print(" " if output[x] == "0" else "*", end = '')

if __name__ == "__main__":
    # execute only if run as a script
    main()
