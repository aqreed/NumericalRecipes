"""
    Unit tests of the betai function

    Expected values extracted from:
        [URL] https://www.encyclopediaofmath.org/index.php/Incomplete_beta-function
"""


import pytest
import nr
from os import system
from subprocess import check_output
from numpy.testing import assert_almost_equal


def test_betai_x0():
    """
        Checks betai output for x = 0
    """
    a, b, x = 0.5, 0.5, 0

    calculated_value = nr.betai(a, b, x)
    expected_value = 0

    assert_almost_equal(calculated_value, expected_value)


def test_betai_x1():
    """
        Checks betai output for x = 1
    """
    a, b, x = 0.5, 0.5, 1

    calculated_value = nr.betai(a, b, x)
    expected_value = 1

    assert_almost_equal(calculated_value, expected_value)


def test_betai_symmetry():
    """
        Checks relation Ix(a, b) = 1 - Ix-1(b, a)
    """
    a, b, x = 1, 10, 0.15

    calculated_value = nr.betai(a, b, x) + nr.betai(b, a, 1 - x)
    expected_value = 1

    assert_almost_equal(calculated_value, expected_value)


def test_betai_recurrence():
    """
        Checks relation Ix(a, b) = xIx(a−1, b) + (1−x)Ix(a, b−1)
    """
    a, b, x = 1, 10, 0.15

    calculated_value = nr.betai(a, b, x) - x * nr.betai(a - 1, b, x) - \
                       (1 - x) * nr.betai(a, b - 1, x)

    expected_value = 0

    assert_almost_equal(calculated_value, expected_value)
