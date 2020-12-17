import re
import typing
from dataclasses import dataclass, field


@dataclass
class Passport:
    byr: typing.Optional[int] = field(default=None)
    iyr: typing.Optional[int] = field(default=None)
    eyr: typing.Optional[int] = field(default=None)
    hgt: typing.Optional[str] = field(default=None)
    hcl: typing.Optional[str] = field(default=None)
    ecl: typing.Optional[str] = field(default=None)
    pid: typing.Optional[str] = field(default=None)
    cid: typing.Optional[int] = field(default=None)

    def validate(self):
        for each in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
            if not getattr(self, each):
                return False

        return True

    def validate_2(self):
        if not self.validate():
            return False
        if not 1920 <= self.byr <= 2002:
            return False
        if not 2010 <= self.iyr <= 2020:
            return False
        if not 2020 <= self.eyr <= 2030:
            return False
        if not self.hgt.endswith('cm') and not self.hgt.endswith('in'):
            return False
        height_digits = re.findall(r'\d+', self.hgt)
        height_number = int(height_digits[0])
        if self.hgt.endswith('in') and not 59 <= height_number <= 76:
            return False
        elif self.hgt.endswith('cm') and not 150 <= height_number <= 193:
            return False
        if self.hcl[0] != '#' or not self.hcl[1:].isalnum():
            return False
        if self.ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
        if len(self.pid) != 9:
            return False

        return True


def solve_both(file_name: str) -> typing.Tuple[int, int]:
    with open(file_name, 'r') as f:
        passport_data = f.readlines()
    passports = []
    passport = Passport()
    for line in passport_data:
        if line == '\n':
            # Separator
            passports.append(passport)
            passport = Passport()
            continue
        line_data = line.strip().split(' ')
        for item in line_data:
            key_value = item.strip().split(':')
            if key_value[0] in ('byr', 'iyr', 'eyr', 'cid'):
                setattr(passport, key_value[0], int(key_value[1]))
            else:
                setattr(passport, key_value[0], key_value[1])

    valid_count = 0
    valid_2_count = 0
    for each in passports:
        if each.validate():
            valid_count += 1
        if each.validate_2():
            valid_2_count += 1

    return valid_count, valid_2_count
