from functools import reduce
from typing import List


def _parse_matrix(grid: str) -> List[list]:
    lines = grid.split()
    matrix: List[list] = []
    line_counter = 0
    for line in lines:
        symbols = list(line)
        matrix.insert(line_counter, symbols)
        line_counter += 1

    return matrix


def solve_first(grid: str) -> int:
    matrix = _parse_matrix(grid)
    track_width = len(matrix[0])
    pos_x = 3
    pos_y = 1
    tree_counter = 0
    while pos_y < len(matrix):
        if pos_x > (track_width - 1):
            # Wrapping
            pos_x = pos_x - track_width
        if matrix[pos_y][pos_x] == '#':
            tree_counter += 1
            matrix[pos_y][pos_x] = 'X'
        else:
            matrix[pos_y][pos_x] = 'O'
        pos_x += 3
        pos_y += 1
    # Nice matrix printer
    # print('\n')
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

    return tree_counter


def solve_second(grid: str, slopes: List[tuple]) -> int:
    matrix = _parse_matrix(grid)
    track_width = len(matrix[0])
    tree_counts = []
    for slope in slopes:
        pos_x = slope[0]
        pos_y = slope[1]
        tree_counter = 0
        while pos_y < len(matrix):
            if pos_x > (track_width - 1):
                # Wrapping
                pos_x = pos_x - track_width
            if matrix[pos_y][pos_x] == '#':
                tree_counter += 1
            pos_x += slope[0]
            pos_y += slope[1]

        tree_counts.append(tree_counter)

    return reduce((lambda x, y: x * y), tree_counts)
