from typing import Tuple


def _parse_single_string(boarding_pass: str) -> Tuple[int, int]:
    start = 0
    end = 127
    for char in boarding_pass[:7]:
        if char == 'F':
            end = int((start + end + 1) / 2) - 1
        elif char == 'B':
            start = int((start + end + 1) / 2)

    row = start
    start = 0
    end = 7

    for char in boarding_pass[7:]:
        if char == 'L':
            end = int((start + end + 1) / 2) - 1
        elif char == 'R':
            start = int((start + end + 1) / 2)

    column = start

    return row, column


def solve_first(boarding_passes: list) -> int:
    rows_cols = [_parse_single_string(x) for x in boarding_passes]
    ids = [x[0] * 8 + x[1] for x in rows_cols]

    return max(ids)


def solve_second(boarding_passes: list) -> int:
    rows_cols = [_parse_single_string(x) for x in boarding_passes]
    ids = [x[0] * 8 + x[1] for x in rows_cols]
    all_possible_ids = range(min(ids), max(ids))

    return [x for x in all_possible_ids if x not in ids][0]
