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


def test_gammaln1():
    x = 0.01

    calculated_value = float((check_output(['./test_gammaln',
                             str(x)])).decode("utf-8").split('\n')[0])
    expected_value = 4.599479878042021722514

    assert_almost_equal(calculated_value, expected_value)


def test_gammaln2():
    x = 1.0

    calculated_value = float((check_output(['./test_gammaln',
                             str(x)])).decode("utf-8").split('\n')[0])
    expected_value = 0

    assert_almost_equal(calculated_value, expected_value)


def test_gammaln3():
    x = 2.0

    calculated_value = float((check_output(['./test_gammaln',
                             str(x)])).decode("utf-8").split('\n')[0])
    expected_value = 0

    assert_almost_equal(calculated_value, expected_value)


def test_gammaln4():
    x = 5.0

    calculated_value = float((check_output(['./test_gammaln',
                              str(x)])).decode("utf-8").split('\n')[0])
    expected_value = 3.178053830347945619647

    assert_almost_equal(calculated_value, expected_value)
