"""
Count number of valid passwords
"""
from itertools import filterfalse


def main():
    # Use a breakpoint in the code line below to debug your script.
    with open('passwords.txt') as f:
        passwords = [data.strip().split(' ') for data in f]

    print(list(passwords))

    result = filterfalse(lambda x: not (int(x[0].split('-')[0]) <= x[2].count(x[1][0]) <= int(x[0].split('-')[1])), passwords)

    print('Number of valid passwords:', len(list(result)))


if __name__ == '__main__':
    main()
