
import numpy as np
import pytest
from adventcode.day4 import update_board, check_winner, refresh


@pytest.fixture
def test_board():
    return np.array([[67, 57,  2, 21, 19],
                     [11, 79, 74, 45, 95],
                     [42, 90, 68, 47, 62],
                     [80, 61,  1,  0, 39],
                     [43, 76, 40, 27, 66]])


@pytest.fixture
def test_file():
    return refresh


@pytest.mark.parametrize("test_board, num, expected", [
    (None, 90,  np.array([[67, 57,  2, 21, 19],
                         [11, 79, 74, 45, 95],
                          [42, -1, 68, 47, 62],
                          [80, 61,  1,  0, 39],
                          [43, 76, 40, 27, 66]])),
    (None, 999, np.array([[67, 57,  2, 21, 19],
                          [11, 79, 74, 45, 95],
                          [42, 90, 68, 47, 62],
                          [80, 61,  1,  0, 39],
                          [43, 76, 40, 27, 66]])),
    (None, 0, np.array([[67, 57,  2, 21, 19],
                       [11, 79, 74, 45, 95],
                        [42, 90, 68, 47, 62],
                        [80, 61,  1,  -1, 39],
                        [43, 76, 40, 27, 66]]))
], indirect=["test_board"])
def test_update_board(test_board, num, expected):
    np.testing.assert_array_equal(
        update_board(num, test_board), expected)


@pytest.mark.parametrize("test_board, expected", [
    (np.array([[67, 57,  2, 21, 19],
               [11, 79, 74, 45, 95],
               [42, 90, 68, 47, 62],
               [-1, -1,  -1,  -1, -1],
               [43, 76, 40, 27, 66]]), True),
    (np.array([[67, 57,  2, -1, 19],
               [11, 79, 74, -1, 95],
               [42, 90, 68, -1, 62],
               [80, 61,  1,  -1, 39],
               [43, 76, 40, -1, 66]]), True),
    (np.array([[67, 57,  2, 21, 19],
               [11, 79, 74, 45, 95],
               [42, 90, 68, 47, 62],
               [80, 61,  1,  -1, 39],
               [43, 76, 40, 27, 66]]), False),
    (np.array([[67, 57,  2, 21, 19],
               [11, 79, 74, 45, 95],
               [42, 90, 68, 47, 62],
               [-1, -1,  -1,  -1, 39],
               [43, 76, 40, 27, 66]]), False)
])
def test_check_winner(test_board, expected):
    assert check_winner(test_board) == expected


def test_nums_parse_type():
    nums, _ = refresh('./input/day4sample.txt')
    assert isinstance(nums, list)


def test_nums_parse_length():
    nums, _ = refresh('./input/day4sample.txt')
    assert len(nums) == 27


def test_boards_parse_type():
    _, boards = refresh('./input/day4sample.txt')
    assert isinstance(boards, list)


def test_boards_parse_length():
    _, boards = refresh('./input/day4sample.txt')
    assert len(boards) == 3


def tests_boards_are_numpy():
    _, boards = refresh('./input/day4sample.txt')
    types = set([type(board) for board in boards])
    assert (len(types) == 1) and (isinstance(boards[0], np.ndarray))
