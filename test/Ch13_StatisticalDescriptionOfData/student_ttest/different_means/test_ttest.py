"""
    Unit tests of the Student t-test for difference of means

    Expected values obtained from SciPy stats library
"""
import pytest
import numericalrecipes as nr
import numpy as np
from scipy.stats import ttest_ind
from numpy.testing import assert_almost_equal


def test_ttest_0():
    """
        Checks against SciPy function
    """
    data1 = np.array([1, 22, 3, 4, 5, 16, 7, 8, 9])
    data2 = np.array([1.1, 2, 3, 4, 5, 6, 7, 18, 9])

    # Student's "t"
    calculated_value = nr.ttest(data1, data2)[0]
    expected_value = ttest_ind(data1, data2)[0]

    assert_almost_equal(calculated_value, expected_value, 4)

    # Student's "significance"
    calculated_value = nr.ttest(data1, data2)[1]
    expected_value = ttest_ind(data1, data2)[1]

    assert_almost_equal(calculated_value, expected_value, 4)


def test_ttest_1():
    """
        Checks against SciPy function
    """
    data1 = np.array([1, 22, 3, 4, 5, 16])
    data2 = np.array([1.1, 2, 3, 4, 5, 6, 7, 18, 9])

    # Student's "t"
    calculated_value = nr.ttest(data1, data2)[0]
    expected_value = ttest_ind(data1, data2)[0]

    assert_almost_equal(calculated_value, expected_value, 4)

    # Student's "significance"
    calculated_value = nr.ttest(data1, data2)[1]
    expected_value = ttest_ind(data1, data2)[1]

    assert_almost_equal(calculated_value, expected_value, 4)
