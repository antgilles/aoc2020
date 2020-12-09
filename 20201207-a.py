#!/usr/bin/python

from aocd.models import Puzzle

def parents(searched, bags, par=None):
    if par == None:
        par = []
    for bag, contenus in bags.items():
        for nb, name in contenus:
            if name == searched:
                if bag not in par:
                    par.append(bag)
                    parents(bag, bags, par)
    return par

def main():
    puzzle = Puzzle(year=2020, day=7)
    lines = puzzle.input_data.split('\n')
    bags = {}

    for line in lines:
        contenant = ' '.join(line.split(" contain ")[0].split(' ')[:-1])
        bags[contenant]=[]
        contenus = line.split(" contain ")[1]

        for contenu in contenus.split(', '):
            if contenu[-1]=='.':
                contenu = contenu[:-1]
            bags[contenant].append((contenu.split(' ')[0],' '.join(contenu.split(' ')[1:-1])))
    par = parents('shiny gold', bags)
    print(len(par))



if __name__ == "__main__":
    # execute only if run as a script
    main()


