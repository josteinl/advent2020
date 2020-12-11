"""
Day 10 - Jolts
"""


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


if __name__ == '__main__':
    # Part one:
    result = part_one()
    print(f'Result {result}')

    # result = part_two()
    # print(f'Result {result}')
