import pytest
import numpy as np
from adventcode.day15 import expand


@pytest.mark.parametrize("data, expected", [
    ([[1, 1], [1, 1]], [[1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
                        [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
                        [2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                        [2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                        [3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
                        [3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
                        [4, 4, 5, 5, 6, 6, 7, 7, 8, 8],
                        [4, 4, 5, 5, 6, 6, 7, 7, 8, 8],
                        [5, 5, 6, 6, 7, 7, 8, 8, 9, 9],
                        [5, 5, 6, 6, 7, 7, 8, 8, 9, 9]]),
    ([[8]], [[8, 9, 1, 2, 3],
             [9, 1, 2, 3, 4],
             [1, 2, 3, 4, 5],
             [2, 3, 4, 5, 6],
             [3, 4, 5, 6, 7]])
])
def test_expand(data, expected):
    arr = expand(data)

    np.testing.assert_array_equal(arr, expected)
