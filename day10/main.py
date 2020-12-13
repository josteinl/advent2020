"""
Day 10 - Jolts
"""
import itertools
import operator
from datetime import datetime


def part_one():
    with open('data.txt', 'r') as f:
        numbers = [int(data) for data in f]

    numbers.sort()
    print(numbers)

    jolt = 0
    ones = 0
    threes = 0

    for position, output_joltage in enumerate(numbers):
        if jolt <= output_joltage <= jolt + 3:
            print('jolt:', jolt, 'new jolt', output_joltage)
            if output_joltage - jolt == 1:
                ones += 1
            elif output_joltage - jolt == 3:
                threes += 1
            jolt = output_joltage
            continue
        else:
            print('ERROR!')

    # Add device 3 jolts
    threes += 1

    return ones * threes


def valid_combination(variant, max_joltage):
    """
    Too slow!

    Test run with this method (test2-data.txt):
    valid_combinations: 19208
    Time used: 0:03:06.881566

    Return True if variant is a valid combination
    """
    joltage = 0
    for adaper_joltage in variant:
        if joltage < adaper_joltage <= joltage + 3:
            joltage = adaper_joltage
        else:
            return False

    return joltage < max_joltage <= joltage + 3


def valid_combination_two(variant, max_joltage):
    """
    Faster ?

    Test run with this method (test2-data.txt):
    Current valid combinations for iteration 30 : 1
    Current valid combinations for iteration 29 : 16
    Current valid combinations for iteration 28 : 121
    Current valid combinations for iteration 27 : 572
    Current valid combinations for iteration 26 : 1889
    Current valid combinations for iteration 25 : 4628
    Current valid combinations for iteration 24 : 8759
    Current valid combinations for iteration 23 : 13268
    Current valid combinations for iteration 22 : 16751
    Current valid combinations for iteration 21 : 18560
    Current valid combinations for iteration 20 : 19127
    Current valid combinations for iteration 19 : 19208
    Fount no more combinations, quit
    valid_combinations: 19208
    0:06:15.025115


    Return True if variant is a valid combination
    """
    # firs element must be at right distance
    if not 0 < variant[0] <= 3:
        return False

    if not max_joltage - 3 <= variant[-1] < max_joltage:
        return False

    return all(1 <= diff <= 3 for diff in map(operator.sub, variant[1:], variant[:-1]))


def part_two():
    """
    Find how many distinct arrangements that reach the max joltage
    """
    with open('data.txt', 'r') as f:
        numbers = [int(data) for data in f]

    numbers.sort()
    print(numbers)

    max_joltage = numbers[-1]
    # Remove last (number = max_joltage)
    numbers = numbers[:-1]
    numbers_length = len(numbers)
    valid_combinations = 0
    last_valid_count = 0
    finished = False
    while not finished:
        for variant in itertools.combinations(numbers, numbers_length):
            valid_combinations += valid_combination(variant, max_joltage)

        if last_valid_count == valid_combinations:
            print('Fount no more combinations, quit')
            finished = True
            break
        last_valid_count = valid_combinations
        print('Current valid combinations for iteration', numbers_length, ':', valid_combinations)
        numbers_length -= 1
        if numbers_length == 1:
            finished = True

    print('valid_combinations:', valid_combinations)
    return valid_combinations


if __name__ == '__main__':
    # result = part_one()
    # print(f'Result {result}')
    start_time = datetime.now()
    part_two()
    time_elapsed = datetime.now() - start_time
    print(time_elapsed)
