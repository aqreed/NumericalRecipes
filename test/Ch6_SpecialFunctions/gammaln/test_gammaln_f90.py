"""
    Python interface for the unit tests of the
    Log Gamma Fortran function.

    Expected values extracted from:
        [URL] https://keisan.casio.com/exec/system/1180573442
"""
import pytest
import numpy as np
from os import system, chdir, getcwd
from subprocess import check_output
from numpy.testing import assert_almost_equal


# Compile the Fortran tests source code to object files
# the next chdir and stuff is needed due to pytest working from root dir
path2fortran_source = '../../../src/numericalrecipes/Ch6_SpecialFunctions/gammaln'
path2fortran_test = 'test/Ch6_SpecialFunctions/gammaln'

owd = getcwd()
chdir(path2fortran_test)

system('gfortran -c ' + path2fortran_source + '/gammaln.f90 test_gammaln.f90')
system('gfortran gammaln.o test_gammaln.o -o ftest_gammaln')  # Link objects
system('rm *.o *.mod')  # Remove unnecessary objects and module

chdir(owd)


# Fortran interface function
def fortran_gammaln(x):
    return float((check_output([owd + '/' + path2fortran_test + '/ftest_gammaln',
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

    assert_almost_equal(calculated_value, expected_value, 4)


def test_gammaln_recurrence():
    """
        Gamma function satisfies the recurrence relation:
            gamma(z+1) = z * gamma(z)

        Accordingly, this test checks that gamma log satisfies:
            gammaln(z+1) = ln(z) + gammaln(z)
    """

    x1, x2, x3, x4 = 0.001, 1.1, 3.32, 23.11

    c1 = fortran_gammaln(x1 + 1) - (np.log(x1) + fortran_gammaln(x1))
    c2 = fortran_gammaln(x2 + 1) - (np.log(x2) + fortran_gammaln(x2))
    c3 = fortran_gammaln(x3 + 1) - (np.log(x3) + fortran_gammaln(x3))
    c4 = fortran_gammaln(x4 + 1) - (np.log(x4) + fortran_gammaln(x4))

    calculated_value = [c1, c2, c3, c4]
    expected_value = [0, 0, 0, 0]

    assert_almost_equal(calculated_value, expected_value, 4)
