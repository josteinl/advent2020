"""
Day 11 - Seating
"""

from itertools import chain
import collections


def occupied_count(seating):
    return ''.join(chain.from_iterable(seating)).count('#')


def adjacent_occupied(x, y, seating):
    occupied = 0
    # Above
    for look_x in range(x - 1, x + 2):
        for look_y in range(y - 1, y + 2):
            if look_x == x and look_y == y:
                continue
            if seating[look_y][look_x] == '#':
                occupied += 1
    return occupied


def sit_down(seating, dim_x, dim_y):
    return_seating = seating.copy()
    for y in range(1, dim_y):
        for x in range(1, dim_x):
            occupied = adjacent_occupied(x, y, seating)
            if seating[y][x] == 'L' and occupied == 0:
                # Empty seat
                # and no adjacent occupied
                return_seating[y] = return_seating[y][:x] + '#' + return_seating[y][x + 1:]
            elif seating[y][x] == '#' and occupied >= 4:
                # Occupied and 4 or more adjecent seats, raise up
                return_seating[y] = return_seating[y][:x] + 'L' + return_seating[y][x + 1:]

    return return_seating


def see_occupied_in_direction(x, y, dir_x, dir_y, seating):
    max_x = len(seating[0]) - 1
    max_y = len(seating) - 1
    cur_x = x
    cur_y = y

    cur_x += dir_x
    cur_y += dir_y
    while 0 <= cur_x <= max_x and 0 <= cur_y <= max_y:
        if seating[cur_y][cur_x] == '#':
            return 1
        elif seating[cur_y][cur_x] == 'L':
            return 0

        cur_x += dir_x
        cur_y += dir_y

    return 0


def seen_occupied(x, y, seating):
    occupied = 0
    for look_x in range(- 1, + 2):
        for look_y in range(- 1, + 2):
            if look_x == 0 and look_y == 0:
                continue
            occupied += see_occupied_in_direction(x, y, look_x, look_y, seating)
    return occupied


def sit_down_part_two(seating, dim_x, dim_y):
    return_seating = seating.copy()
    for y in range(0, dim_y):
        for x in range(0, dim_x):
            occupied = seen_occupied(x, y, seating)
            if seating[y][x] == 'L' and occupied == 0:
                # Empty seat
                # and no adjacent occupied
                return_seating[y] = return_seating[y][:x] + '#' + return_seating[y][x + 1:]
            elif seating[y][x] == '#' and occupied >= 5:
                # Occupied and 5 or more seen seats, raise up
                return_seating[y] = return_seating[y][:x] + 'L' + return_seating[y][x + 1:]

    return return_seating


def part_two():
    with open('data.txt', 'r') as f:
        seating = [data.strip() for data in f]

    dimension_x = len(seating[0])
    dimension_y = len(seating)

    last_seating = None

    while collections.Counter(last_seating) != collections.Counter(seating):
        last_seating = seating.copy()
        seating = sit_down_part_two(seating, dimension_x, dimension_y)
    return occupied_count(last_seating)


def part_one():
    with open('data.txt', 'r') as f:
        seating = [data.strip() for data in f]

    dimension_x = len(seating[0])
    dimension_y = len(seating)

    # Extend seating with empty space all around, makes it easier to count later
    for row_number in range(dimension_y):
        seating[row_number] = '.' + seating[row_number] + '.'
    seating = ['.' * (dimension_x + 2)] + seating + ['.' * (dimension_x + 2)]

    last_seating = None

    while collections.Counter(last_seating) != collections.Counter(seating):
        last_seating = seating.copy()
        seating = sit_down(seating, dimension_x + 1, dimension_y + 1)

    return occupied_count(last_seating)


if __name__ == '__main__':
    # Part one:
    # result = part_one()
    # print(f'Result {result}')

    result = part_two()
    print(f'Result {result}')
