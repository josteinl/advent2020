"""
Day 6. Count number of yes answers
"""

import operator
from functools import reduce


def count_unique_answers(group):
    group = group.strip().replace('\n', '')
    return len(set(group))


def count_all_yes_answers(group):
    # Make list of person, with a set for an individual persons answer
    persons = [set(answers) for answers in group.split('\n')]
    # Intersect groups answers
    result = reduce(operator.and_, persons)
    return len(result)


def main():
    with open('data.txt', 'r') as f:
        data = f.read()

    groups = data.split('\n\n')
    print(f'Number of groups: {len(groups)}')
    total_yes_answers = 0
    total_all_yes_answers = 0
    for group in groups:
        total_yes_answers += count_unique_answers(group)
        total_all_yes_answers += count_all_yes_answers(group)

    print(f'Total number of yes answers (part I): {total_yes_answers}')
    print(f'Total number of group all yes answers (part II): {total_all_yes_answers}')


if __name__ == '__main__':
    main()
