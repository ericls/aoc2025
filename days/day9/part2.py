from functools import lru_cache
from itertools import combinations, cycle, islice

from lib.input import get_input
from lib.path import Pt

data = get_input()

lines = data.splitlines()

pts = [Pt(*map(int, line.split(","))) for line in lines]

sides = [
    (a, b) for a, b in islice(zip(cycle(pts), islice(cycle(pts), 1, None)), len(pts))
]


@lru_cache(maxsize=len(pts))
def pt_in_sides(pt: Pt):
    c = 0
    for a, b in sides:
        if a.y == b.y:
            if a.y == pt.y:
                min_x, max_x = min(a.x, b.x), max(a.x, b.x)
                if min_x <= pt.x <= max_x:
                    return True
            else:
                continue
        elif a.x < pt.x:
            continue
        elif a.x == pt.x:
            min_y, max_y = min(a.y, b.y), max(a.y, b.y)
            if min_y <= pt.y <= max_y:
                return True
        else:
            min_y, max_y = sorted([a.y, b.y])
            if min_y <= pt.y < max_y:
                c += 1
    return c % 2 == 1


def seg_seg_intersect(seg1: tuple[Pt, Pt], seg2: tuple[Pt, Pt]):
    a1, b1 = seg1
    a2, b2 = seg2
    v = None
    h = None
    if a1.x == b1.x:
        if a2.x == b2.x:
            return False
        else:
            v = (a1, b1)
            h = (a2, b2)
    else:
        if a2.y == b2.y:
            return False
        else:
            v = (a2, b2)
            h = (a1, b1)
    v1, v2 = v
    h1, h2 = h
    if min(v1.y, v2.y) < h1.y < max(v1.y, v2.y) and min(h1.x, h2.x) < v1.x < max(
        h1.x, h2.x
    ):
        return True
    return False


@lru_cache(maxsize=len(pts))
def seg_intersect_sides(seg: tuple[Pt, Pt]):
    return any(seg_seg_intersect(seg, side) for side in sides)


def rect_in_sides(a: Pt, b: Pt):
    x1, x2 = sorted([a.x, b.x])
    y1, y2 = sorted([a.y, b.y])
    corners = [Pt(x1, y1), Pt(x2, y1), Pt(x2, y2), Pt(x1, y2)]
    c1, c2, c3, c4 = corners
    segs = [(c1, c2), (c2, c3), (c3, c4), (c4, c1)]
    if not all(pt_in_sides(c) for c in corners):
        return False
    if any(seg_intersect_sides(seg) for seg in segs):
        return False
    return True


def size_if_valid(a: Pt, b: Pt):
    if not rect_in_sides(a, b):
        return 0
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)


def sol():
    return max(size_if_valid(*pair) for pair in combinations(pts, 2))


print(sol())
