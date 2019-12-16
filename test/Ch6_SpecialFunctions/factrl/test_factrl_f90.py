"""
    Python interface for the unit tests of the
    factorial Fortran function.

    Expected values extracted from Numpy Math
"""
import numpy as np
from os import system, chdir, getcwd
from subprocess import check_output
import unittest as ut


# Compile the Fortran tests source code to object files
# the next chdir and stuff is needed due to pytest working from root dir
path2fortran_source = '../../../src/numericalrecipes/Ch6_SpecialFunctions/factrl'
path2fortran_mod = '../../../src/numericalrecipes/Ch6_SpecialFunctions/gammaln'
path2fortran_test = 'test/Ch6_SpecialFunctions/factrl'

owd = getcwd()
chdir(path2fortran_test)

system('gfortran -c ' + path2fortran_mod + '/gammaln.f90')  # compile gammaln
system('gfortran -c ' + path2fortran_source + '/factrl.f90 test_factrl.f90')
system('gfortran gammaln.o factrl.o test_factrl.o -o ftest_factrl')  # Link objects
system('rm *.o *.mod')  # Remove unnecessary objects and module

chdir(owd)


# Fortran interface function
def fortran_factrl(x):
    return float((check_output([owd + '/' + path2fortran_test + '/ftest_factrl',
                 str(x)])).decode("utf-8").split('\n')[0])


class Test_factrl_input(ut.TestCase):
    """
        Checks values
    """
    def test_fctrl(self):
        c1 = 1 - fortran_factrl(1)
        c2 = 120 - fortran_factrl(5)
        c3 = np.math.factorial(10) - fortran_factrl(10)
        c4 = np.math.factorial(15) - fortran_factrl(15)
        c5 = np.math.factorial(20) - fortran_factrl(20)

        calculated_value = [c1, c2, c3, c4, c5]
        expected_value = [0, 0, 0, 0, 0]
        self.assertEqual(calculated_value, expected_value)
