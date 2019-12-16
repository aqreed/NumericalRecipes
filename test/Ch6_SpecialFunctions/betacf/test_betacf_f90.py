"""
    Unit tests of the betacf function

    Expected values obtained from Aroian, L.A. "Continued Fractions for
    the Incomplete Beta Function" (1941), Ann. Math. Statist. 218-223
    [URL] https://projecteuclid.org/download/pdf_1/euclid.aoms/1177731751

    Requires previous compilation of Fortran source code:

        $ gfortran -c lib_stat.f90 test_betai.f90
        $ gfortran lib_stat.o test_betai.o -o fmain_test_betai
"""
from os import system, chdir, getcwd
from subprocess import check_output
from numpy.testing import assert_almost_equal


# Compile the Fortran tests source code to object files
# the next chdir and stuff is needed due to pytest working from root dir
path2fortran_source = '../../../src/numericalrecipes/Ch6_SpecialFunctions/betacf'
path2fortran_test = 'test/Ch6_SpecialFunctions/betacf'

owd = getcwd()
chdir(path2fortran_test)

system('gfortran -c ' + path2fortran_source + '/betacf.f90 test_betacf.f90')  # compile betai and test
system('gfortran betacf.o test_betacf.o -o ftest_betacf')  # Link objects
system('rm *.o *.mod')  # Remove unnecessary objects and module

chdir(owd)


# Fortran interface function
def fortran_betacf(a, b, x):
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
        return float(check_output([owd + '/' + path2fortran_test + '/ftest_betacf',
                                   a, b, x]).decode("utf-8").split('\n')[0])


def test_betacf():
    """
        Checks betai output
    """
    a, b, x = 2.5, 1.5, 0.5

    calculated_value = fortran_betacf(a, b, x)
    expected_value = 2.260324

    assert_almost_equal(calculated_value, expected_value, 4)
