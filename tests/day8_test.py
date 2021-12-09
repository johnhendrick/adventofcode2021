import pytest
import numpy as np
from adventcode.day8 import length_search


@pytest.mark.parametrize("np_array_in, size, expected", [
    (np.array(['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf',
     'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec']), 2, 'gc'),
    (np.array(['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf',
     'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec']), 4, 'gfec'),
    (np.array(['edbfga', 'begcd', 'bcg', 'gc', 'gcadebf',
     'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec']), 3, 'bcg'),
    (np.array(['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf',
     'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec']), 7, 'gcadebf')
])
def test_length_search(np_array_in, size, expected):
    assert length_search(np_array_in, size) == expected
