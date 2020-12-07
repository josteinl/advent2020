"""
Day 7. Handy Haversacks
"""


def convert_to_dict(bag_rule):
    key, value = bag_rule.split(' contain ')
    value_list = value.split(', ')
    if value_list == ['no other']:
        value_dict = {}
    else:
        value_dict = {}
        for value in value_list:
            number, color = value.split(' ', 1)
            value_dict[color] = int(number)
    return {key: value_dict}


def find_direct_containing(rules, param):
    """
    return list of all rules that directly contain param
    """

    return_list = []
    for rule in rules:
        if param in rules[rule]:
            return_list.append(rule)

    return return_list


def count_required_containing_bags(rules, bag_name):
    return_count = 0
    for bag in rules[bag_name]:
        if isinstance(rules[bag_name], dict):
            return_count += rules[bag_name][bag] + rules[bag_name][bag] * count_required_containing_bags(rules, bag)
        else:
            return_count += rules[bag_name]

    # print(f'{bag_name} must contain {return_count} bags')
    return return_count


def main():
    with open('data.txt', 'r') as f:
        # Read and remove ',', '.', 'bags', 'bag'
        bag_rules = [data.replace('.', '').replace(' bags', '').replace(' bag', '').strip() for data in f]

    rules = {}
    for rule in bag_rules:
        rules.update(convert_to_dict(rule))

    # print(f'Rules dict: {rules}')

    # Part 1
    # How many bag colors can eventually contain at least one shiny gold bag?
    # This is a bad implementation, and does not got into several layers of bags :-(
    contain_shiny_gold = find_direct_containing(rules, 'shiny gold')

    for sub_find in contain_shiny_gold:
        contain_shiny_gold += find_direct_containing(rules, sub_find)

    contain_shiny_gold = set(contain_shiny_gold)

    print(f'How many bag colors can eventually contain at least one shiny gold (part I): {len(contain_shiny_gold)}')

    # Part 2
    # How many individual bags are required inside your single shiny gold bag?
    count = count_required_containing_bags(rules, 'shiny gold')

    print(f'How many individual bags are required inside your single shiny gold bag? (part II): {count}')


if __name__ == '__main__':
    main()
