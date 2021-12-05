import pytest
from adventcode.day5 import traverse_manhattan, traverse_diagonal


@pytest.mark.parametrize("start_coor, end_coor, expected", [
    ((0, 9), (5, 9),    [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]),
    ((7, 0), (7, 4),    [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)]),
    ((0, 9), (2, 9),    [(0, 9), (1, 9), (2, 9)]),
    ((3, 4), (1, 4),    [(3, 4), (2, 4), (1, 4)])
])
def test_traverse_manhattan(start_coor, end_coor, expected):
    result = traverse_manhattan(start_coor, end_coor)
    print(result)
    assert result == expected


@pytest.mark.parametrize("start_coor, end_coor, expected", [
    ((0, 0), (5, 5),    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
    ((3, 3), (0, 0),    [(3, 3), (2, 2), (1, 1), (0, 0)]),
    ((4, 4), (6, 2),    [(4, 4), (5, 3), (6, 2)]),
    ((5, 0), (3, 2),    [(5, 0), (4, 1), (3, 2)])
])
def test_traverse_diagonal(start_coor, end_coor, expected):
    result = traverse_diagonal(start_coor, end_coor)
    print(result)
    assert result == expected
