"""
Count number of valid passwords
"""
from itertools import filterfalse


def part1():
    with open('passwords.txt') as f:
        passwords = [data.strip().split(' ') for data in f]

    print(list(passwords))

    result = filterfalse(lambda x: not (int(x[0].split('-')[0]) <= x[2].count(x[1][0]) <= int(x[0].split('-')[1])), passwords)

    print('Number of valid passwords:', len(list(result)))


def part2():
    with open('passwords.txt') as f:
        passwords = [data.strip().split(' ') for data in f]

    print(list(passwords))

    # pos1 = int(x[0].split('-')[0])-1
    # pos2 = int(x[0].split('-')[1])-1
    # pwd = x[2]
    # chr = x[1][0]
    # ^ = bitwise xor
    # bool(pwd[pos1]==chr) ^ bool(pwd[pos2]==chr)
    result = list(filterfalse(lambda x: not(bool(x[2][int(x[0].split('-')[0])-1] == x[1][0]) ^ bool(x[2][int(x[0].split('-')[1])-1] == x[1][0])), passwords))

    print(result)
    print('Number of valid passwords:', len(result))


if __name__ == '__main__':
    # part1()
    part2()
