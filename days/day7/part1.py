from lib.input import get_input_lines

lines = get_input_lines()


def sol():
    beams_at_row = [[lines[0].index("S")]]
    split_count = 0
    while len(beams_at_row) < len(lines):
        last_row_beams = beams_at_row[-1]
        row = lines[len(beams_at_row)]
        current_row_beams = set()
        for col in last_row_beams:
            if row[col] == "^":
                split_count += 1
                current_row_beams.add(col - 1)
                current_row_beams.add(col + 1)
            else:
                current_row_beams.add(col)
        current_row_beams = list(current_row_beams)
        beams_at_row.append(current_row_beams)
    return split_count


print(sol())
