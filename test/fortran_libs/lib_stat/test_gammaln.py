"""
    Unit tests of the Log Gamma function

    Expected values extracted from:
        [URL] https://keisan.casio.com/exec/system/1180573442

    Requires previous compilation of Fortran source code:

        $ gfortran -c lib_stat.f90 test_gammaln.f90
        $ gfortran lib_stat.o test_gammaln.o -o test_gammaln
"""


import pytest

from subprocess import check_output
from numpy.testing import assert_almost_equal


def test_gammaln():
    c1 = float((check_output(['./test_gammaln',
                str(0.01)])).decode("utf-8").split('\n')[0])

    c2 = float((check_output(['./test_gammaln',
                str(1.0)])).decode("utf-8").split('\n')[0])

    c3 = float((check_output(['./test_gammaln',
                str(2.0)])).decode("utf-8").split('\n')[0])

    c4 = float((check_output(['./test_gammaln',
                str(5.0)])).decode("utf-8").split('\n')[0])

    calculated_value = [c1, c2, c3, c4]
    expected_value = [4.599479878042021722514, 0, 0, 3.178053830347945619647]

    assert_almost_equal(calculated_value, expected_value)
