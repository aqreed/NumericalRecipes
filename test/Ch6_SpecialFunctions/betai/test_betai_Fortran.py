"""
    Unit tests of the betai function

    Expected values extracted from:
        [URL] https://www.encyclopediaofmath.org/index.php/Incomplete_beta-function

    Requires previous compilation of Fortran source code:

        $ gfortran -c lib_stat.f90 test_betai.f90
        $ gfortran lib_stat.o test_betai.o -o fmain_test_betai
"""


import pytest
from os import system, chdir, getcwd
from subprocess import check_output
from numpy.testing import assert_almost_equal


# Compile the Fortran tests source code to object files
# the next chdir and stuff is needed due to pytest working from root dir
path2fortran_source = '../../../src/nr/Ch6_SpecialFunctions/betai'
path2fortran_mod1 = '../../../src/nr/Ch6_SpecialFunctions/betacf'
path2fortran_mod2 = '../../../src/nr/Ch6_SpecialFunctions/gammaln'
path2fortran_test = 'test/Ch6_SpecialFunctions/betai'

owd = getcwd()
chdir(path2fortran_test)

system('gfortran -c ' + path2fortran_mod1 + '/betacf.f90')  # compile betacf
system('gfortran -c ' + path2fortran_mod2 + '/gammaln.f90')  # compile gammaln
system('gfortran -c ' + path2fortran_source + '/betai.f90 test_betai.f90')  # compile betai and test
system('gfortran betacf.o gammaln.o betai.o test_betai.o -o ftest_betai')  # Link objects
system('rm *.o *.mod')  # Remove unnecessary objects and module

chdir(owd)


# Fortran interface function
def fortran_betai(a, b, x):
    if (a < 0):
        print('Wrong value for a')
    elif (b < 0):
        print('Wrong value for b')
    if (x < 0 or x > 1):
        print('Wrong value for x')
    else:
        a = str(a)
        b = str(b)
        x = str(x)
        return float(check_output([owd + '/' + path2fortran_test + '/ftest_betai',
                                   a, b, x]).decode("utf-8").split('\n')[0])


def test_betai_x0():
    """
        Checks betai output for x = 0
    """
    a, b, x = 0.5, 0.5, 0

    calculated_value = fortran_betai(a, b, x)
    expected_value = 0

    assert_almost_equal(calculated_value, expected_value)


def test_betai_x1():
    """
        Checks betai output for x = 1
    """
    a, b, x = 0.5, 0.5, 1

    calculated_value = fortran_betai(a, b, x)
    expected_value = 1

    assert_almost_equal(calculated_value, expected_value)


def test_betai_symmetry():
    """
        Checks relation Ix(a, b) = 1 - Ix-1(b, a)
    """
    a, b, x = 1, 10, 0.15

    calculated_value = fortran_betai(a, b, x) + fortran_betai(b, a, 1 - x)
    expected_value = 1

    assert_almost_equal(calculated_value, expected_value)


def test_betai_recurrence():
    """
        Checks relation Ix(a, b) = xIx(a−1, b) + (1−x)Ix(a, b−1)
    """
    a, b, x = 1, 10, 0.15

    calculated_value = fortran_betai(a, b, x) - \
                       x * fortran_betai(a - 1, b, x) - \
                       (1 - x) * fortran_betai(a, b-1, x)

    expected_value = 0

    assert_almost_equal(calculated_value, expected_value)
