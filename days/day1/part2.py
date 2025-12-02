from operator import sub, add
from lib.input import get_input_lines

lines = get_input_lines()

def sol():
    cur = 50
    zero_count = 0

    for line in lines:
        direction, distance = line[0], int(line[1:])
        op = add if direction == "R" else sub
        i = cur
        for _ in range(distance):
            i = op(i, 1) % 100
            if i == 0:
                zero_count += 1
        cur = i
    
    return zero_count

print(sol())