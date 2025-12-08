from lib.input import get_input
from itertools import product


data = get_input()
lines = data.splitlines()
nodes = [tuple(map(int, line.split(","))) for line in lines]

pairs = product(nodes, repeat=2)

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


def sol():
    islands = {k: set([k]) for k in nodes}
    node_to_island_key = {k: k for k in nodes}

    def connect(a, b):
        a_island_key = node_to_island_key[a]
        b_island_key = node_to_island_key[b]
        a_island = islands[a_island_key]
        b_island = islands[b_island_key]

        if a_island_key == b_island_key:
            return

        new_island = a_island | b_island
        new_island_key = min(new_island)
        del islands[a_island_key]
        del islands[b_island_key]
        islands[new_island_key] = new_island
        for node in new_island:
            node_to_island_key[node] = new_island_key

    for i in range(len(distance_map)):
        _, (a, b) = sorted_distance_conn_pair[i]
        connect(a, b)
        if len(islands) == 1:
            return a[0] * b[0]


print(sol())
