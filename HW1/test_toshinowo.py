"""
This python script handles the testing of the find_max_val_unimodal_arr()
function from hw1.py.
"""

__author__ = "Tolulope Oshinowo"
import pytest
from hw1 import find_max_val_unimodal_arr

test_cases = [
    # Test with nominal odd-length array
    [5, 4, 3, 2, 1], # input unimodal list with max at start
    [1, 2, 3, 4, 5, 4, 3, 2, 1], # input unimodal list with max at center
    [1, 2, 3, 4], # input unimodal list with max at end
    [1, 4, 8, 12, 23, 54, 95, 110, 200, 145, 72, 35], # input unimodal list with max at center and skips
    [3, 3, 3, 3, 3], # input unimodal list with all equal
    [1, 5], # two values
    [2], # one value
    [], # no values
]

@pytest.mark.timeout(1)
@pytest.mark.parametrize("test_case", test_cases)
def test_find_max_val_unimodal_arr(test_case):
    """
    This function assesses whether or not the find_max_val_unimodal_arr()
    is working properly by trying different scenarios and edge cases for
    finding the maximum in a unimodal list
    """
    assert find_max_val_unimodal_arr(test_case) == -1 or find_max_val_unimodal_arr(test_case) == max(test_case), "Test failed for %s" % (test_case)
    # When pytest is run, each item in the test_cases list will be used as the test_case argument for this function. Use
    # an assert statement to assert that the output your function returns
