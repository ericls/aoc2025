from operator import sub, add
from lib.input import get_input_lines

lines = get_input_lines()

def sol():
    cur = 50

    zero_count = 0

    for line in lines:
        direction, distance = line[0], int(line[1:])
        op = add if direction == "R" else sub
        cur = op(cur, distance) % 100
        if cur == 0:
            zero_count += 1
    
    return zero_count

print(sol())