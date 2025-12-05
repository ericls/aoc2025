from lib.input import get_input

data = get_input()

range_lines, id_lines = data.split("\n\n")


ranges = [
    tuple(map(int, line.split('-')))
    for line in range_lines.splitlines()
]

ids = [
    int(line)
    for line in id_lines.splitlines()
]

def is_valid(id):
    for (a, b) in ranges:
        if a <= id <= b:
            return True
    return False


def sol():
    return sum(is_valid(id) for id in ids)

print(sol())