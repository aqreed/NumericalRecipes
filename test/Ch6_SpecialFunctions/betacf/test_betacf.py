"""
    Unit tests of the betacf function

    Expected values obtained from Aroian, L.A. "Continued Fractions for
    the Incomplete Beta Function" (1941), Ann. Math. Statist. 218-223
    [URL] https://projecteuclid.org/download/pdf_1/euclid.aoms/1177731751
"""
import pytest
import numericalrecipes as nr
from numpy.testing import assert_almost_equal


def test_betacf():
    """
        Checks betacf output
    """
    a, b, x = 2.5, 1.5, 0.5

    calculated_value = nr.betacf(a, b, x)
    expected_value = 2.260324

    assert_almost_equal(calculated_value, expected_value)
