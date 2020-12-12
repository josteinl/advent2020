"""
Day 12 - Boat navigation
"""
import math


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def part_one():
    with open('data.txt', 'r') as f:
        instructions = [(data[0], int(data[1:])) for data in f]

    # east
    current_direction = 90
    current_north = 0
    current_east = 0

    for instruction, units in instructions:
        if instruction == 'F':
            if current_direction == 0:
                current_north += units
            elif current_direction == 90:
                current_east += units
            elif current_direction == 180:
                current_north -= units
            elif current_direction == 270:
                current_east -= units

        elif instruction == 'L':
            current_direction = (current_direction - units) % 360
        elif instruction == 'R':
            current_direction = (current_direction + units) % 360
        elif instruction == 'N':
            current_north += units
        elif instruction == 'S':
            current_north -= units
        elif instruction == 'E':
            current_east += units
        elif instruction == 'W':
            current_east -= units

    return abs(current_north) + abs(current_east)


def part_two():
    with open('data.txt', 'r') as f:
        instructions = [(data[0], int(data[1:])) for data in f]

    current_north = 0
    current_east = 0

    waypoint_north = 1
    waypoint_east = 10

    for instruction, units in instructions:
        if instruction == 'F':
            current_north += units * waypoint_north
            current_east += units * waypoint_east

        elif instruction == 'L':
            waypoint_east, waypoint_north = rotate((0, 0), (waypoint_east, waypoint_north), math.radians(units))
        elif instruction == 'R':
            waypoint_east, waypoint_north = rotate((0, 0), (waypoint_east, waypoint_north), math.radians(-units))
        elif instruction == 'N':
            waypoint_north += units
        elif instruction == 'S':
            waypoint_north -= units
        elif instruction == 'E':
            waypoint_east += units
        elif instruction == 'W':
            waypoint_east -= units

    return abs(current_north) + abs(current_east)


if __name__ == '__main__':
    # Part one:
    # result = part_one()
    # print(f'Result {result}')

    result = part_two()
    print(f'Result {result}')
