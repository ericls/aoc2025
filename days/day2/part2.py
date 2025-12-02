import re
from lib.input import get_input

regex = re.compile(r"^(\d+)(\1)+$")

lines = get_input().split(",")

def is_invalid(i):
    return next(regex.finditer(str(i)), False)

def sol():
    invalids = []
    for line in lines:
        a, b = line.split("-")
        a, b = int(a), int(b)
        for i in range(a, b + 1):
            if is_invalid(i):
                invalids.append(i)
    return sum(invalids)

print(sol())
