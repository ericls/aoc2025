from operator import add, mul
from lib.input import get_input
from functools import reduce


data = get_input(strip=False)

rows = [[seg for seg in row.split(" ") if seg] for row in data.splitlines()]


def eval_col(col):
    *operands, op = [row[col] for row in rows]
    return reduce(add if op == "+" else mul, map(int, operands))


def sol():
    return sum(map(eval_col, range(len(rows[0]))))


print(sol())
