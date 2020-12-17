from day2.main import part1, part2


def test_part1():
    assert len(part1('day2/test-passwords.txt')) == 2


def test_part2():
    assert len(part2('day2/test-passwords.txt')) == 1
