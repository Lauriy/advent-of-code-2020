from typing import List


def solve_first(numbers: List[int]) -> int:
    for each1 in numbers:
        for each2 in numbers:
            if each1 + each2 == 2020:
                return each1 * each2


def solve_second(numbers: List[int]) -> int:
    for each1 in numbers:
        for each2 in numbers:
            for each3 in numbers:
                if each1 + each2 + each3 == 2020:
                    return each1 * each2 * each3
