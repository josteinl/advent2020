"""
Day 8 - program
"""


def part_one():
    with open('data.txt', 'r') as f:
        program = [data.split() for data in f]

    accumulator = 0
    position = 0
    print(program)

    while position < len(program) and program[position][0] != 'seen':
        last_position = position
        if program[position][0] == 'acc':
            accumulator += int(program[position][1])
            position += 1
        elif program[position][0] == 'nop':
            position += 1
        elif program[position][0] == 'jmp':
            position += int(program[position][1])
        program[last_position][0] = 'seen'

    return accumulator


def part_two():
    with open('test-data.txt', 'r') as f:
        program = [data.split() for data in f]

    seen = [False] * len(program)
    accumulator = 0
    position = 0
    print(program)

    look_ahead = True

    while position < len(program):

        if look_ahead:
            # Look ahead if next operation has been run before (seen)
            # If next operation has been seen before, then possible change this operation (if nop or jmp)
            seen_next_operation = False
            if program[position][0] == 'nop':
                seen_next_operation = seen[position+1]
            elif program[position][0] == 'jmp':
                seen_next_operation = seen[position+int(program[position][1])]

            if seen_next_operation:
                if program[position][0] == 'nop':
                    program[position][0] = 'jmp'
                    look_ahead = False
                elif program[position][0] == 'jmp':
                    program[position][0] = 'nop'
                    look_ahead = False

        seen[position] = True

        if program[position][0] == 'acc':
            accumulator += int(program[position][1])
            position += 1
        elif program[position][0] == 'nop':
            position += 1
        elif program[position][0] == 'jmp':
            position += int(program[position][1])


        print(program)
    print(f'{seen}')
    return accumulator


if __name__ == '__main__':
    # Part one:
    # result = part_one()
    # print(f'Result {result}')

    result = part_two()
    print(f'Result {result}')
