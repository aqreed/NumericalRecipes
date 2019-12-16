"""
    Python interface for the unit tests of the "tutest" Fortran function.
    Contains the wrapper function and the tests.

    Expected values obtained from SciPy
"""
from re import findall
from os import system, chdir, getcwd
from subprocess import run
from scipy.stats import ttest_ind
from numpy.testing import assert_almost_equal


# Compile the Fortran tests source code to object files
path2Ch13 = '../../../../src/numericalrecipes/Ch13_StatisticalDescriptionOfData/'
path2Ch6 = '../../../../src/numericalrecipes/Ch6_SpecialFunctions/'
path2fortran_test = 'test/Ch13_StatisticalDescriptionOfData/student_ttest/different_variances/'

owd = getcwd()
chdir(path2fortran_test)  # chdir is needed due to pytest working from root dir
system('gfortran -c ' + path2Ch6 + 'betacf/betacf.f90')
system('gfortran -c ' + path2Ch6 + 'gammaln/gammaln.f90')
system('gfortran -c ' + path2Ch6 + 'betai/betai.f90')
system('gfortran -c ' + path2Ch13 + 'avevar/avevar.f90')
system('gfortran -c ' + path2Ch13 + 'student_ttest/different_variances/tutest.f90')
system('gfortran -c test_tutest.f90')
system('gfortran avevar.o betai.o betacf.o gammaln.o \
        tutest.o test_tutest.o -o ftest_tutest')  # Link objects
system('rm *.o *.mod')  # Remove unnecessary objects and module
chdir(owd)


# Fortran wrapper function
def fortran_tutest(data1, data2):
    aux = [str(len(data1))]
    aux += [str('') + str(s) + str('') for s in data1]
    aux.insert(0, owd + '/' + path2fortran_test + 'ftest_tutest')

    aux_ = [str(len(data2))]
    aux_ += [str('') + str(s) + str('') for s in data2]
    aux += aux_

    result = run(aux, capture_output=True)
    list_ = findall(r"\d+\.\d+", result.stdout.decode("utf-8"))
    return [float(i) for i in list_]  # returns student's t and significance


def test_tutest_0():
    """
        Checks against SciPy function
    """
    data1 = [1, 22, 3, 4, 5, 16, 7, 8, 9]
    data2 = [1.1, 2, 3, 4, 5, 6, 7, 18, 9]

    # Student's "t"
    calculated_value = fortran_tutest(data1, data2)[0]
    expected_value = ttest_ind(data1, data2, equal_var=False)[0]

    assert_almost_equal(calculated_value, expected_value, 4)

    # Student's "significance"
    calculated_value = fortran_tutest(data1, data2)[1]
    expected_value = ttest_ind(data1, data2, equal_var=False)[1]

    assert_almost_equal(calculated_value, expected_value, 4)


def test_tutest_1():
    """
        Checks against SciPy function
    """
    data1 = [1, 22, 3, 4, 5, 16, 17, 18, 99]
    data2 = [1.1, 2, 3, 4, 5, 6, 7, 18, 9]

    # Student's "t"
    calculated_value = fortran_tutest(data1, data2)[0]
    expected_value = ttest_ind(data1, data2, equal_var=False)[0]

    assert_almost_equal(calculated_value, expected_value, 4)

    # Student's "significance"
    calculated_value = fortran_tutest(data1, data2)[1]
    expected_value = ttest_ind(data1, data2, equal_var=False)[1]

    assert_almost_equal(calculated_value, expected_value, 4)
