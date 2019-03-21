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


def run_fortran_gammaln(x):
    return float((check_output(['./test_gammaln',
                 str(x)])).decode("utf-8").split('\n')[0])


def test_gammaln():
    """
        Checks four values >
    """
    x1, x2, x3, x4 = 0.01, 1.0, 2.0, 5.0

    c1 = run_fortran_gammaln(x1)
    c2 = run_fortran_gammaln(x2)
    c3 = run_fortran_gammaln(x3)
    c4 = run_fortran_gammaln(x4)

    calculated_value = [c1, c2, c3, c4]
    expected_value = [4.599479878042021722514, 0,
                      0, 3.178053830347945619647]

    assert_almost_equal(calculated_value, expected_value)
