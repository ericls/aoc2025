from functools import reduce
from operator import mul
from lib.input import get_input
from itertools import product


data = get_input()
lines = data.splitlines()
nodes = [tuple(map(int, line.split(","))) for line in lines]

pairs = product(nodes, repeat=2)

n = 1000


distance_map = {}


def get_key(a, b):
    return tuple(sorted([a, b]))


for a, b in pairs:
    key = get_key(a, b)
    if key in distance_map:
        continue
    if a == b:
        continue
    distance = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
    distance_map[key] = distance

sorted_distance_conn_pair = sorted([(v, k) for k, v in distance_map.items()])
assert len(distance_map) == len(distance_map), "oh no"


graph = {}

for i in range(n):
    d, (a, b) = sorted_distance_conn_pair[i]
    graph.setdefault(a, set()).add(b)
    graph.setdefault(b, set()).add(a)

islands = []
queue = list(graph.keys())

visited = set()

while queue:
    node = queue.pop()
    if node in visited:
        continue
    island = set()

    def add_to_island(n):
        island.add(n)
        visited.add(n)
        for ns in graph[n]:
            if ns not in visited and ns not in island:
                add_to_island(ns)

    add_to_island(node)

    islands.append(island)


def sol():
    return reduce(mul, sorted([len(island) for island in islands], reverse=True)[:3])


print(sol())
