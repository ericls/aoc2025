from lib.input import get_input

data = get_input()

range_lines, id_lines = data.split("\n\n")

ranges = [
    tuple(map(int, line.split('-')))
    for line in range_lines.splitlines()
]


def sol():
    rs = sorted(ranges)
    counted_to = 0
    c = 0
    for (a, b) in rs:
        if not (b > a):
            print("wtf", counted_to, a, b)
        lower = max(counted_to, a)
        if lower <= b:
            c += (b - lower + 1)
            counted_to = (b + 1)
    return c

print(sol())