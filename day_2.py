from typing import List, NamedTuple


class ParsedInputLine(NamedTuple):
    letter: str
    min: int
    max: int
    password: str


def _parse_rule_and_password(input_line: str) -> ParsedInputLine:
    parts = input_line.split(': ')
    password = parts[1]
    parts = parts[0].split(' ')
    letter = parts[1]
    parts = parts[0].split('-')
    min_occurrences = int(parts[0])
    max_occurrences = int(parts[1])

    return ParsedInputLine(letter=letter, min=min_occurrences, max=max_occurrences, password=password)


def solve_first(inputs: List[str]) -> int:
    matches = 0
    for each in inputs:
        parsed = _parse_rule_and_password(each)
        if parsed.min <= parsed.password.count(parsed.letter) <= parsed.max:
            matches += 1

    return matches


def solve_second(inputs: List[str]) -> int:
    number_of_valid = 0
    for each in inputs:
        parsed = _parse_rule_and_password(each)
        matches = 0
        if parsed.password[parsed.min - 1] == parsed.letter:
            matches += 1
        if parsed.password[parsed.max - 1] == parsed.letter:
            matches += 1
        if matches == 1:
            number_of_valid += 1

    return number_of_valid
