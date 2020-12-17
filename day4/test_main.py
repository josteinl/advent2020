from day4.main import main


def test_valid_passport():
    assert main('day4/test-data.txt') == 2
