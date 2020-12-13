"""
Day 13 - Bus
"""


def part_one():
    with open('data.txt') as f:
        numbers = [data.replace('x', '0') for data in f]

    print(numbers)

    arrive_at_bus_stop = int(numbers[0])
    print(arrive_at_bus_stop)
    routes = list(filter(lambda x: x, map(int, numbers[1].split(','))))

    time_to_next_departure = []
    # time_to_wait_departure = []
    for route in routes:
        time_to_next_departure.append((arrive_at_bus_stop // route) * route + route)
        # time_to_wait_departure.append(arrive_at_bus_stop % route)

    print('bus', routes)
    print('you arrive', arrive_at_bus_stop)
    print('next departure', time_to_next_departure)
    # print('wait for next bus', time_to_wait_departure)
    index = time_to_next_departure.index(min(time_to_next_departure))

    bus_number = routes[index]
    wait_time = time_to_next_departure[index] - arrive_at_bus_stop
    print('-' * 20)
    print('bus', bus_number)
    print('time to wait', wait_time)
    return bus_number * wait_time


if __name__ == '__main__':
    result = part_one()
    print('Result', result)
