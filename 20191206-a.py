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

#data = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L".split('\n')

astro = {}
for obj in data:
    parent = obj.split(')')[0]
    child = obj.split(')')[1]
    if parent not in astro:
        astro[parent] = [child]
    else:
        astro[parent].append(child)
    if child not in astro:
        astro[child] = []

links = 0
for parent, childlist in astro.items():
    links += len(recursive_dfs(astro, parent)) - 1

print(links)

#puzzle.answer_a(str(total_fuel))
