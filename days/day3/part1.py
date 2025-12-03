from days.day3.day3lib import get_value_for_line
from lib.input import get_input_lines

lines = get_input_lines()


def sol():
    return sum(get_value_for_line(line, 2) for line in lines)


print(sol())
