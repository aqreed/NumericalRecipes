"""
    Python interface for the unit tests of the
    Log Gamma C++ function.

    Expected values extracted from:
        [URL] https://keisan.casio.com/exec/system/1180573442
"""
import numpy as np
from os import system, chdir, getcwd
from subprocess import check_output
from numpy.testing import assert_almost_equal


# Compile the C++ tests source code to object files the next
# chdir and stuff is needed due to pytest working from root dir
path2cpp_source = '../../../src/numericalrecipes/Ch6_SpecialFunctions/gammaln'
path2cpp_test = 'test/Ch6_SpecialFunctions/gammaln'

owd = getcwd()
chdir(path2cpp_test)

system('g++ ' + path2cpp_source + '/gammaln.cpp test_gammaln.cpp -o cpptest_gammaln')

chdir(owd)


# C++ interface function
def cpp_gammaln(x):
    return float((check_output([owd + '/' + path2cpp_test + '/cpptest_gammaln',
                 str(x)])).decode("utf-8").split('\n')[0])


def test_gammaln():
    """
        Checks values x > 0
    """
    x1, x2, x3, x4 = 0.01, 1.0, 2.0, 5.0

    c1 = cpp_gammaln(x1)
    c2 = cpp_gammaln(x2)
    c3 = cpp_gammaln(x3)
    c4 = cpp_gammaln(x4)

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

    c1 = cpp_gammaln(x1 + 1) - (np.log(x1) + cpp_gammaln(x1))
    c2 = cpp_gammaln(x2 + 1) - (np.log(x2) + cpp_gammaln(x2))
    c3 = cpp_gammaln(x3 + 1) - (np.log(x3) + cpp_gammaln(x3))
    c4 = cpp_gammaln(x4 + 1) - (np.log(x4) + cpp_gammaln(x4))

    calculated_value = [c1, c2, c3, c4]
    expected_value = [0, 0, 0, 0]

    assert_almost_equal(calculated_value, expected_value, 4)


def test_gammaln_factorial():
    """
        Gamma function satisfies the recurrence relation for
        positive integer values:
            gamma(z) = (z-1)!

        Accordingly, this test checks that gamma log satisfies:
            exp[gammaln(z)] = (z-1)!
    """
    x1, x2, x3, x4 = 1, 2, 6, 9

    c1 = np.exp(cpp_gammaln(x1)) - np.math.factorial(x1 - 1)
    c2 = np.exp(cpp_gammaln(x2)) - np.math.factorial(x2 - 1)
    c3 = np.exp(cpp_gammaln(x3)) - np.math.factorial(x3 - 1)
    c4 = np.exp(cpp_gammaln(x4)) - np.math.factorial(x4 - 1)

    calculated_value = [c1, c2, c3, c4]
    expected_value = [0, 0, 0, 0]

    assert_almost_equal(calculated_value, expected_value, 4)
