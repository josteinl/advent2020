"""
Day 19 - Monster Messages
"""
from pprint import pprint
import re


def get_search_pattern(rules, rule_number):
    return_pattern = ''
    for sub_pattern in rules[rule_number]:
        if isinstance(sub_pattern, int):
            return_pattern += get_search_pattern(rules, sub_pattern)
        elif sub_pattern == '|':
            return_pattern += ')' + sub_pattern + '('
        else:
            return_pattern += sub_pattern

    if '|' in rules[rule_number]:
        return '((' + return_pattern + '))'
    return '(' + return_pattern + ')'

    return return_pattern

def convert_to_string_or_int(rule_list):
    ret_list = []
    for rule in rule_list:
        if rule[0] == '"':
            ret_list.append(rule[1:-1])
        else:
            try:
                ret_list.append(int(rule))
            except Exception:
                ret_list.append(rule)
    return ret_list


def part_one(testfile):
    with open(testfile, 'r') as f:
        data = f.read()

    rule_lines, messages = data.split('\n\n')

    rules = {}
    for rule_line in rule_lines.split('\n'):
        rule_number, rule_line = rule_line.split(':')
        rule_list = rule_line.strip().split(' ')
        rules[int(rule_number)] = convert_to_string_or_int(rule_list)

    # pprint(rules)
    search_pattern = '^' + get_search_pattern(rules, 0) + '$'
    # pprint(search_pattern)

    # pprint(messages)

    # Search for valid messages
    x = re.findall(search_pattern, messages, re.MULTILINE)

    return len(x)


if __name__ == '__main__':
    # Part one:
    valid_messages = part_one('data.txt')
    print(f'valid messages {valid_messages}')
