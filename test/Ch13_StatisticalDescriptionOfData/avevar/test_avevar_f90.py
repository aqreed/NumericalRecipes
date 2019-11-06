"""
    Python interface for the unit tests of the
    avevar Fortran function.

    Expected values obtained from:
        [URL] http://www.alcula.com/calculators/statistics/variance/
"""
import pytest
from re import findall
from os import system, chdir, getcwd
from subprocess import run
from numpy.testing import assert_almost_equal


# Compile the Fortran tests source code to object files
path2fortran_source = '../../../src/numericalrecipes/Ch13_StatisticalDescriptionOfData/avevar'
path2fortran_test = 'test/Ch13_StatisticalDescriptionOfData/avevar'

owd = getcwd()
chdir(path2fortran_test)  # chdir is needed due to pytest working from root dir
system('gfortran -c ' + path2fortran_source + '/avevar.f90 test_avevar.f90')
system('gfortran avevar.o test_avevar.o -o ftest_avevar')  # Link objects
system('rm *.o *.mod')  # Remove unnecessary objects and module
chdir(owd)


# Fortran wrapper function
def fortran_avevar(data):
    aux = [str('') + str(s) + str('') for s in data]
    aux.insert(0, owd + '/' + path2fortran_test + '/ftest_avevar')

    result = run(aux, capture_output=True)
    list_ = findall(r"\d+\.\d+", result.stdout.decode("utf-8"))
    return [float(i) for i in list_]


def test_avevar_10():
    """
        Checks average values of an input dataset
    """
    data = [1, 1, 1, 1, 1]
    calculated_value = fortran_avevar(data)[0]
    expected_value = 1.0

    assert_almost_equal(calculated_value, expected_value, 4)


def test_avevar_11():
    """
        Checks average values of an input dataset
    """
    data = [-2, -1, 0, 1, 2]
    calculated_value = fortran_avevar(data)[0]
    expected_value = 0.0

    assert_almost_equal(calculated_value, expected_value, 4)


def test_avevar_12():
    """
        Checks average values of an input dataset
    """
    data = [1, 2, 3, 4, 5]
    calculated_value = fortran_avevar(data)[0]
    expected_value = 3

    assert_almost_equal(calculated_value, expected_value, 4)


def test_avevar_20():
    """
        Checks variance (sample) values of an input dataset
    """
    data = [1, 1, 1, 1, 1]
    calculated_value = fortran_avevar(data)[1]
    expected_value = 0.0

    assert_almost_equal(calculated_value, expected_value, 4)


def test_avevar_21():
    """
        Checks variance (sample) values of an input dataset
    """
    data = [1, 2, 3, 4, 5]
    calculated_value = fortran_avevar(data)[1]
    expected_value = 2.5

    assert_almost_equal(calculated_value, expected_value, 4)


def test_avevar_22():
    """
        Checks variance (sample) values of an input dataset
    """
    data = [1, 3, 5, 7, 9]
    calculated_value = fortran_avevar(data)[1]
    expected_value = 10.0

    assert_almost_equal(calculated_value, expected_value, 4)
