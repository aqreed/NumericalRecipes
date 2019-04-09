"""
    Unit tests of the Log Gamma function

    Expected values extracted from:
        [URL] https://keisan.casio.com/exec/system/1180573442

    Requires previous compilation of Fortran source code:

        $ gfortran -c lib_stat.f90 test_gammaln.f90
        $ gfortran lib_stat.o test_gammaln.o -o fmain_test_gammaln
"""


import pytest

from os import system
from subprocess import check_output
from numpy.testing import assert_almost_equal


# Compilation of fortran code
system('python compile_fortran.py')

def fortran_gammaln(x):
    return float((check_output(['./fmain_test_gammaln',
                 str(x)])).decode("utf-8").split('\n')[0])


def test_gammaln():
    """
        Checks values x > 0
    """
    x1, x2, x3, x4 = 0.01, 1.0, 2.0, 5.0

    c1 = fortran_gammaln(x1)
    c2 = fortran_gammaln(x2)
    c3 = fortran_gammaln(x3)
    c4 = fortran_gammaln(x4)

    calculated_value = [c1, c2, c3, c4]
    expected_value = [4.599479878042021722514, 0,
                      0, 3.178053830347945619647]

    assert_almost_equal(calculated_value, expected_value)


def test_gammaln_recurrence():
    """
        Gamma log function satisfies the recurrence relation:
            gamma(z+1) = z * gamma(z)

        Accordingly, this test checks that:
            gammaln(z+1) = ln(z) + gammaln(z)
    """

    x1, x2, x3, x4 = 0.001, 1.1, 3.32, 23.11

    c1 = fortran_gammaln(x1 + 1) - (log(x1) + fortran_gammaln(x1))
    c2 = fortran_gammaln(x2 + 1) - (log(x2) + fortran_gammaln(x2))
    c3 = fortran_gammaln(x3 + 1) - (log(x3) + fortran_gammaln(x3))
    c4 = fortran_gammaln(x4 + 1) - (log(x4) + fortran_gammaln(x4))

    calculated_value = [c1, c2, c3, c4]
    expected_value = [0, 0, 0, 0]

    assert_almost_equal(calculated_value, expected_value)
