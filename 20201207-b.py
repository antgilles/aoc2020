#!/usr/bin/python

from aocd.models import Puzzle

def recursive_dfs(bags, node, num):
    res = 0
    for nb, name in bags[node]:
        if nb != "no":
            res += recursive_dfs(bags, name, int(nb))
        else:
            return num
    return num * (res + 1)


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
            bags[contenant].append(((contenu.split(' ')[0]),' '.join(contenu.split(' ')[1:-1])))
    result = recursive_dfs( bags, 'shiny gold', 1)
    print(result - 1)



if __name__ == "__main__":
    # execute only if run as a script
    main()


