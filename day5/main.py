"""
Day 5
"""


def decode_seat_string(seat):
    """
    Test data

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

    Seat string is 10 bits binary

    B = 1
    F = 0
    R = 1
    L = 0
    """
    bin_seat_number = seat.replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1')
    return int(bin_seat_number, 2)


def main():
    with open('data.txt') as f:
        seats = [decode_seat_string(data.strip()) for data in f]

    seats.sort()
    for position in range(len(seats) - 1):
        if seats[position + 1] - seats[position] != 1:
            print(f'Seats that are apart: {seats[position]} {seats[position + 1]}')
            print(f'Your seat is {seats[position] + 1}')

    print(f'Max seat number: {max(seats)}')


if __name__ == '__main__':
    main()
