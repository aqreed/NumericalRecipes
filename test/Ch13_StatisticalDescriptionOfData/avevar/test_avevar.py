"""
    Unit tests of the avevar function

    Expected values extracted from:
        [URL] http://www.alcula.com/calculators/statistics/variance/
"""


import pytest
import numericalrecipes as nr
from numpy.testing import assert_almost_equal


def test_avevar_10():
    """
        Checks average values of an input dataset
    """
    data = [1, 1, 1, 1, 1]
    calculated_value = nr.avevar(data)[0]
    expected_value = 1.0

    assert_almost_equal(calculated_value, expected_value)


def test_avevar_11():
    """
        Checks average values of an input dataset
    """
    data = [-2, -1, 0, 1, 2]
    calculated_value = nr.avevar(data)[0]
    expected_value = 0.0

    assert_almost_equal(calculated_value, expected_value)


def test_avevar_12():
    """
        Checks average values of an input dataset
    """
    data = [1, 2, 3, 4, 5]
    calculated_value = nr.avevar(data)[0]
    expected_value = 3

    assert_almost_equal(calculated_value, expected_value)


def test_avevar_20():
    """
        Checks variance (sample) values of an input dataset
    """
    data = [1, 1, 1, 1, 1]
    calculated_value = nr.avevar(data)[1]
    expected_value = 0.0

    assert_almost_equal(calculated_value, expected_value)


def test_avevar_21():
    """
        Checks variance (sample) values of an input dataset
    """
    data = [1, 2, 3, 4, 5]
    calculated_value = nr.avevar(data)[1]
    expected_value = 2.5

    assert_almost_equal(calculated_value, expected_value)


def test_avevar_22():
    """
        Checks variance (sample) values of an input dataset
    """
    data = [1, 3, 5, 7, 9]
    calculated_value = nr.avevar(data)[1]
    expected_value = 10.0

    assert_almost_equal(calculated_value, expected_value)
