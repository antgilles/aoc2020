#!/usr/bin/python
import math
from aocd.models import Puzzle

def recursive_dfs(graph, node, visited=None):
    if visited is None:
        visited = []

    if node not in visited:
        visited.append(node)

    unvisited = [n for n in graph[node] if n not in visited]

    for node in unvisited:
        recursive_dfs(graph, node, visited)

    return visited

puzzle = Puzzle(year=2019, day=6)
data = puzzle.input_data.split('\n')

#data = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN".split('\n')

astro = {}
for obj in data:
    parent = obj.split(')')[0]
    child = obj.split(')')[1]
    if child not in astro:
        astro[child] = [parent]
    else:
        astro[child].append(parent)
    if parent not in astro:
        astro[parent] = []

print(astro)

links = 0
cur = "YOU"
pathyou = []
while len(astro[cur]) > 0:
    pathyou.append(cur)
    cur = astro[cur][0]
print(pathyou)

common = None
cur = "SAN"
pathsanta = []
while len(astro[cur]) > 0:
    pathsanta.append(cur)
    cur = astro[cur][0]
    if cur in pathyou:
        break

print(pathsanta)
pathyou = pathyou[:pathyou.index(cur)]
print(pathyou)
result = len(pathsanta) + len(pathyou) -2
print(result)

