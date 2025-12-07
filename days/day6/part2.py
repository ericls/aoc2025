from operator import add, mul
from lib.input import get_input
from functools import reduce


data = get_input(strip=False)
lines = data.splitlines()
op_line = lines.pop()

operations = []

for col in range(len(lines[0])):
    maybe_op = op_line[col]
    if maybe_op in ("+", "*"):
        operations.append((maybe_op, []))
    digits = []
    for line in lines:
        digit = line[col]
        if digit == " ":
            continue
        digits.append(int(digit))
    if not digits:
        continue
    num = reduce(lambda acc, d: acc * 10 + d, digits)
    operations[-1][-1].append(num)


def sol():
    return sum(map(lambda op: reduce(add if op[0] == "+" else mul, op[1]), operations))


print(sol())
