"""
Get the list of number. The sum of two of them make the number 2020. Find the pair and multiply them together to find the answer.
"""
from itertools import combinations
from itertools import filterfalse

import operator
from functools import reduce


def main(n=2):
    with open('data.txt') as f:
        numbers = [int(data.strip()) for data in f]

    combines = combinations(numbers, n)

    result2020 = filterfalse(lambda x: sum(x) != 2020, combines)

    [factors] = result2020

    result = reduce(operator.mul, factors, 1)

    print(f'Result n={n}: {result}')


if __name__ == '__main__':
    main(n=2)
    main(n=3)
