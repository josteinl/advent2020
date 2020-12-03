"""
Day 3 - travel through the woods
"""


def main(move_x_direction, move_y_direction):
    tree_hits= 0
    current_x = 0
    current_y = 0

    with open('area.txt') as f:
        rows = [data.strip() for data in f]

    row_len = len(rows[0])

    while current_y < len(rows):
        tree_hits += rows[current_y][current_x % row_len] == '#'
        current_x += move_x_direction
        current_y += move_y_direction

    print(f'tree_hits {tree_hits}')
    return tree_hits


if __name__ == '__main__':
    # Part one:
    tree_hits = main(move_x_direction=3, move_y_direction=1)
    print(f'tree_hits {tree_hits}')

    """
    Part two:
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """
    tree_hits = main(move_x_direction=1, move_y_direction=1)
    tree_hits *= main(move_x_direction=3, move_y_direction=1)
    tree_hits *= main(move_x_direction=5, move_y_direction=1)
    tree_hits *= main(move_x_direction=7, move_y_direction=1)
    tree_hits *= main(move_x_direction=1, move_y_direction=2)
    print(f'tree_hits multiplied {tree_hits}')
