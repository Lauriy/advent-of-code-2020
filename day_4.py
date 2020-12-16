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
        print(self)
        for each in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
            if getattr(self, each) is None:
                print(each)
                return False

        return True


def solve_first(file_name: str) -> int:
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
            key_value = item.split(':')
            if key_value[0] in ('byr', 'iyr', 'eyr', 'cid'):
                key_value[1] = int(key_value[1])
            setattr(passport, key_value[0], key_value[1])

    valid_count = 0
    for each in passports:
        if each.validate():
            valid_count += 1

    return valid_count
