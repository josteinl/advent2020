"""
Day 16: Ticket Translation
"""
from pprint import pprint

from ClusterShell.RangeSet import RangeSet

fields_dict = {}


def part_one():
    with open('data.txt', 'r') as f:
        data = f.read()

    fields, your_ticket, nearby_tickets = data.split('\n\n')

    # Build dictionary of fields and valid ranges
    all_ranges = RangeSet()
    fields = fields.split('\n')
    fields_dict = {}
    for field_line in fields:
        field_name, field_ranges = field_line.split(':')
        field_ranges = field_ranges.split('or')
        for field_range in field_ranges:
            if field_name in fields_dict:
                fields_dict[field_name] = fields_dict[field_name].union(RangeSet(field_range))
            else:
                fields_dict[field_name] = RangeSet(field_range)
            all_ranges = all_ranges.union(RangeSet(field_range))

    # Nearby tickets
    part_one_answer = 0
    nearby_tickets = nearby_tickets.split('\n')[1:]
    for ticket in nearby_tickets:
        for field_value in ticket.split(','):
            if field_value not in all_ranges:
                part_one_answer += int(field_value)

    return part_one_answer

# found at https://cs.lmu.edu/~ray/notes/backtracking/
def solve(values, safe_up_to, size):
    """Finds a solution to a backtracking problem.

    values     -- a sequence of values to try, in order. For a map coloring
                  problem, this may be a list of colors, such as ['red',
                  'green', 'yellow', 'purple']
    safe_up_to -- a function with two arguments, solution and position, that
                  returns whether the values assigned to slots 0..pos in
                  the solution list, satisfy the problem constraints.
    size       -- the total number of “slots” you are trying to fill

    Return the solution as a list of values.
    """
    solution = [None] * size

    def extend_solution(position):
        for value in values:
            solution[position] = value
            if safe_up_to(solution, position):
                if position >= size - 1 or extend_solution(position + 1):
                    return solution
        return None

    return extend_solution(0)


def is_solution_valid(solution_list, top_position):
    """ a function with two arguments, solution and position, that
        returns whether the values assigned to slots 0..pos in
        the solution list, satisfy the problem constraints.
    """
    global fields_dict

    # If list contains duplicates it is wrong:
    if len(solution_list[:top_position + 1]) != len(set(solution_list[:top_position + 1])):
        return False

    for position in range(top_position + 1):
        if position not in fields_dict[solution_list[position]]['possible_indexes']:
            return False

    return True


def part_two():
    with open('data.txt', 'r') as f:
        data = f.read()

    fields, your_ticket, nearby_tickets = data.split('\n\n')

    # Build dictionary of fields and valid ranges
    all_ranges = RangeSet()
    fields = fields.split('\n')
    for field_line in fields:
        field_name, field_ranges = field_line.split(':')
        field_ranges = field_ranges.split('or')
        for field_range in field_ranges:
            if field_name in fields_dict:
                fields_dict[field_name]['range'] = fields_dict[field_name]['range'].union(RangeSet(field_range))
            else:
                fields_dict[field_name] = {'range': RangeSet(field_range),
                                           'possible_indexes': []}
            all_ranges = all_ranges.union(RangeSet(field_range))

    # Nearby tickets
    valid_tickets = []
    nearby_tickets = nearby_tickets.split('\n')[1:]
    for ticket in nearby_tickets:
        all_fields_ok = True
        for field_value in ticket.split(','):
            if field_value not in all_ranges:
                all_fields_ok = False
        if all_fields_ok:
            valid_tickets.append([int(x) for x in ticket.split(',')])

    # Include own ticket to valid_tickets
    your_ticket = [int(x) for x in your_ticket.split('\n')[1].split(',')]
    valid_tickets.append(your_ticket)

    # pprint(valid_tickets, width=120)

    for field in fields_dict:
        for i in range(len(your_ticket)):
            # is field valid for all tickets index i?
            field_valid_for_all = True
            for valid_ticket in valid_tickets:
                if valid_ticket[i] not in fields_dict[field]['range']:
                    field_valid_for_all = False
                    break
            if field_valid_for_all:
                fields_dict[field]['possible_indexes'].append(i)

    pprint(fields_dict, width=120)

    solution = solve(fields_dict.keys(), is_solution_valid, len(fields_dict.keys()))

    result = 1
    for i in range(len(solution)):
        if solution[i].startswith('departure'):
            result *= your_ticket[i]

    return result


if __name__ == '__main__':
    # result = part_one()
    # print('Result', result)
    result = part_two()
    print('Result', result)
