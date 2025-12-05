from lib.input import get_input_lines
from lib.path import Pt

grid = get_input_lines()

def is_accessible(g, p: Pt):
    return (
        len(
            [
                nb
                for nb in p.nb8
                if (not (nb.x < 0 or nb.y < 0 or nb.x >= len(g[0]) or nb.y >= len(g)))
                and (g[nb.y][nb.x] == "@")
            ]
        )
        < 4
    )


def sol():
    return sum(
        [
            is_accessible(grid, Pt(i, j)) if grid[j][i] == "@" else False
            for i in range(len(grid[0]))
            for j in range(len(grid))
        ]
    )


print(sol())
