from itertools import combinations
from lib.input import get_input
from lib.path import Pt


data = get_input()

lines = data.splitlines()

pts = [Pt(*map(int, line.split(","))) for line in lines]


def size(a: Pt, b: Pt):
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)


def sol():
    return max(size(*pair) for pair in combinations(pts, 2))


print(sol())
