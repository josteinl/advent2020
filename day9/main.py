"""
Day 9 - XMAS
"""
from itertools import combinations


def part_one():
    with open('data.txt', 'r') as f:
        numbers = [int(data) for data in f]

    print(numbers)

    preamble = 25

    for position, number in enumerate(numbers[preamble:], start=preamble):
        combines = combinations(numbers[position - preamble:position], 2)
        if number not in [sum(x) for x in combines]:
            return number

    return


if __name__ == '__main__':
    # Part one:
    result = part_one()
    print(f'Result {result}')

    # result = part_two()
    # print(f'Result {result}')
