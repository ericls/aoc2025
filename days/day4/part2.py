from lib.input import get_input_lines
from lib.path import Pt

grid = get_input_lines()
grid = [list(line) for line in grid]

counts = {
    Pt(x, y): 0
    for x in range(len(grid[0]))
    for y in range(len(grid))
}

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "@":
            for nb in Pt(x, y).nb8:
                if nb in counts:
                    counts[nb] += 1


def sol():
    removed_count = 0
    while True:
        removable = [k for k, v in counts.items() if v < 4 and grid[k.y][k.x] == "@"]
        if not removable:
            break
        for r in removable:
            removed_count += 1
            grid[r.y][r.x] = "."
            for nb in r.nb8:
                if nb in counts:
                    counts[nb] -= 1
    return removed_count

print(sol())
