"""
Count number of valid passwords
"""
from itertools import filterfalse


def part1(testfile):
    with open(testfile) as f:
        passwords = [data.strip().split(' ') for data in f]

    return list(filterfalse(lambda x: not (int(x[0].split('-')[0]) <= x[2].count(x[1][0]) <= int(x[0].split('-')[1])), passwords))



def part2(testfile):
    with open(testfile) as f:
        passwords = [data.strip().split(' ') for data in f]

    # pos1 = int(x[0].split('-')[0])-1
    # pos2 = int(x[0].split('-')[1])-1
    # pwd = x[2]
    # chr = x[1][0]
    # ^ = bitwise xor
    # bool(pwd[pos1]==chr) ^ bool(pwd[pos2]==chr)
    return list(filterfalse(lambda x: not (bool(x[2][int(x[0].split('-')[0]) - 1] == x[1][0]) ^ bool(x[2][int(x[0].split('-')[1]) - 1] == x[1][0])), passwords))


if __name__ == '__main__':
    result = part1('passwords.txt')
    print('Number of valid passwords part one:', len(result))

    result = part2('passwords.txt')
    print('Number of valid passwords part two:', len(result))
