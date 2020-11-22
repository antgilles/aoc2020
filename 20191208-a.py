#!/usr/bin/python

from aocd.models import Puzzle

def main():
    puzzle = Puzzle(year=2019, day=8)
    data = puzzle.input_data
    #data = "123456789012"
    wide = 25
    tall = 6

    layers = [data[i: i + tall * wide] for i in range(0, len(data), tall * wide)]
    print(layers)
    chosenlayer = layers[0]
    for layer in layers:
        if chosenlayer.count("0") > layer.count("0"):
            chosenlayer = layer
    print(chosenlayer)
    print(chosenlayer.count("1")*chosenlayer.count("2"))

if __name__ == "__main__":
    # execute only if run as a script
    main()
