import pytest
from adventcode.day12 import clean_blocked


@pytest.mark.parametrize("input_list, max_, expected", [
    (['start', 'A', 'c', 'A', 'b', 'end'], 1, ['start', 'c', 'b', 'end']),
    (['blue', 'blue', 'red', 'pink'], 2, ['blue', 'red', 'pink']),
    (['start', 'ey', 'ey', 'end'], 2, ['start', 'ey', 'end'])
])
def test_clean_blocked(input_list, max_, expected):
    output = set(clean_blocked(input_list, max_))
    assert output == set(expected)
