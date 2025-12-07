from lib.input import get_input_lines
from functools import lru_cache

lines = get_input_lines()


@lru_cache
def num_of_path(row, col):
    if row == len(lines):
        return 1
    if lines[row][col] == "^":
        return num_of_path(row + 1, col - 1) + num_of_path(row + 1, col + 1)
    return num_of_path(row + 1, col)


def sol():
    return num_of_path(0, lines[0].index("S"))


print(sol())
