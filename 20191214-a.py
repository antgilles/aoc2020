#!/usr/bin/python

from aocd.models import Puzzle
import math

def parsedata():
    puzzle = Puzzle(year=2019, day=14)
    reactionlist = puzzle.input_data.split('\n')
    dicoreaction = {}
    for reaction in reactionlist:
        componentlist = reaction.split(' => ')[0].split(', ')
        product = reaction.split(' => ')[1]
        #print(product)
        prodquantity = product.split(' ')[0]
        prodname = product.split(' ')[1]
        dicoreaction[prodname]=[prodquantity, []]
        for component in componentlist:
            #print(component)
            compquantity = component.split(' ')[0]
            compname = component.split(' ')[1]
            dicoreaction[prodname][1].append((compquantity, compname))
    return dicoreaction

def dorecepy(dicoreaction, name, number, left=None):
    nbore = 0
    if left is None:
        left = {}
    if name in left and left[name] >= number:
        left[name] -= number
        print("enough left")
        print(left)

    else:
        if name in left and left[name] < number:
            number -= left[name]
            left[name] = 0
            print(number)
        if name == 'ORE':
            nbore = number
            return nbore, left
        multiplier = math.ceil(number / int(dicoreaction[name][0]))
        print(multiplier)
        if name not in left:
            left[name]=0
        print(name, dicoreaction[name][0], dicoreaction[name][1])
        left[name] += multiplier * int(dicoreaction[name][0]) - number
        print(left)
        for comp in dicoreaction[name][1]:
            res = dorecepy(dicoreaction, comp[1], multiplier * int(comp[0]), left)
            nbore += res[0]
            left = res[1]
    return nbore, left


def main():
    dicoreaction = parsedata()
    print(dicoreaction)

    nbore, left = dorecepy(dicoreaction,"FUEL",1)
    print(nbore,left)
if __name__ == "__main__":
    # execute only if run as a script
    main()
