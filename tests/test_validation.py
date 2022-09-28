import pytest

from q04 import solve

TEST_CASES = [
    ("3 * 2 - 4 * 2 / 3 - 0", "3.33"),
    ("4", "4.00"),
]


@pytest.mark.parametrize("input,expected", TEST_CASES)
def test_solver(input, expected):
    assert solve(input) == expected
