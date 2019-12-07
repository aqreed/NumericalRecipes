"""
    Unit tests of the betai function

    Expected values extracted from:
        [URL] https://www.encyclopediaofmath.org/index.php/Incomplete_beta-function
"""
import pytest
import numericalrecipes as nr
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

    assert_almost_equal(calculated_value, expected_value, 4)


def test_betai_x1():
    """
        Checks betai output for x = 1
    """
    a, b, x = 0.5, 0.5, 1

    calculated_value = nr.betai(a, b, x)
    expected_value = 1

    assert_almost_equal(calculated_value, expected_value, 4)


def test_betai_symmetry():
    """
        Checks relation Ix(a, b) = 1 - I1-x(b, a)
    """
    a, b, x = 1, 10, 0.15

    calculated_value = nr.betai(a, b, x) + nr.betai(b, a, 1 - x)
    expected_value = 1

    assert_almost_equal(calculated_value, expected_value, 4)


def test_betai_recurrence():
    """
        Checks relation Ix(a, a) = 1/2 * I[4x(1−x)](a, 1/2)
    """
    a, b, x = 2, 10, 0.115

    calculated_value = nr.betai(a, a, x) - \
                       (1/2) * nr.betai(a, 1 / 2, 4 * x * (1 - x))
    expected_value = 0

    assert_almost_equal(calculated_value, expected_value, 4)
