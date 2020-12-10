#!/usr/bin/python

from aocd.models import Puzzle

def getdict(lines):
    dict = {}
    for previous in [0, max(lines) +3] + lines :
        dict[previous] = []
        for line in lines:
            diff = line - previous
            if diff > 0 and diff < 4:
                dict[previous].append(line)
    return dict

def dfs(dict, node, visited=None):
    if visited == None:
        visited = {}
    res = 0
    if len(dict[node]) == 0:
        return 1
    for path in dict[node]:
        if path in visited:
            res += visited[path]
        else:
            res += dfs(dict,path,visited)
    visited[node] = res
    return res

def main():
    puzzle = Puzzle(year=2020, day=10)
    lines = puzzle.input_data.split('\n')
    lines = list(map(int, lines))

    dict = getdict(lines)
    res = dfs(dict,0)
    print(res)



if __name__ == "__main__":
    # execute only if run as a script
    main()


