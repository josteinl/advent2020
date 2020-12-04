"""
Day 4 - validate passports
"""
import string


def valid_field(field):
    field_name, data = field.split(':')
    print(f'{field_name}: {data}')
    byr = iyr = eyr = None
    if field_name == 'byr':  # (Birth Year)
        # four digits; at least 1920 and at most 2002.
        byr = int(data)
        return 1920 <= int(data) <= 2002
    elif field_name == 'iyr':  # (Issue Year)
        # four digits; at least 2010 and at most 2020
        iyr = int(data)
        return 2010 <= int(data) <= 2020
    elif field_name == 'eyr':  # (Expiration Year)
        # four digits; at least 2020 and at most 2030.
        eyr = int(data)
        return 2020 <= int(data) <= 2030
    elif field_name == 'hgt':  # (Height)
        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        if 'cm' not in data and 'in' not in data:
            return False
        unit = data[-2:]
        height = int(data[:-2])
        if unit == 'cm':
            return 150 <= int(height) <= 193
        return 59 <= int(height) <= 76
    elif field_name == 'hcl':  # (Hair Color)
        # a # followed by exactly six characters 0-9 or a-f.
        if data[0] != '#':
            return False
        if len(data) != 7:
            return False

        for digit in data[1:]:
            if digit not in string.hexdigits:
                return False
        return True
    elif field_name == 'ecl':  # (Eye Color)
        # exactly one of: amb blu brn gry grn hzl oth.
        return data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field_name == 'pid':  # (Passport ID)
        # a nine-digit number, including leading zeroes.
        if len(data) != 9:
            return False
        for digit in data:
            if digit not in string.digits:
                return False
    return True


def yr_consistency(record):
    """
    Check internal year consistency.
    byr <= iyr <= eyr
    """
    byr = iyr = eyr = None

    fields = record.split()
    for field in fields:
        field_name, data = field.split(':')
        if field_name == 'byr':
            byr = int(data)
        elif field_name =='iyr':
            iyr = int(data)
        elif field_name == 'eyr':
            eyr = int(data)

    return byr <= iyr <= eyr


def valid_passport(record):
    """
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    """
    required_fields = ['byr',  # (Birth Year)
                       'iyr',  # (Issue Year)
                       'eyr',  # (Expiration Year)
                       'hgt',  # (Height)
                       'hcl',  # (Hair Color)
                       'ecl',  # (Eye Color)
                       'pid',  # (Passport ID)
                       # cid (Country ID)
                       ]

    for field in required_fields:
        if f'{field}:' not in record:
            print(f'---** missing field: "{field}" from:\n{record}\n-----')
            return False

    fields = record.split()
    for field in fields:
        if field.startswith('cid:'):
            continue
        if not valid_field(field):
            print(f'---** invalid field: {field} ')
            return False

    if not yr_consistency(record):
        return False

    print('---** Valid passport')
    return True


def main():
    with open('data.txt', 'r') as f:
        data = f.read()

    records = data.split('\n\n')
    print(f'Number of records: {len(records)}')
    valid_passports = 0
    invalid_passports = 0
    for record in records:
        if valid_passport(record):
            valid_passports += 1
        else:
            invalid_passports += 1

    print(f'valid passports {valid_passports}')
    print(f'invalid passports {invalid_passports}')
    return valid_passports


if __name__ == '__main__':
    # Part two:
    valid_passports = main()
    print(f'valid passports {valid_passports}')
