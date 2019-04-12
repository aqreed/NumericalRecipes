"""
    Script to compile the fortran files required to serve as
    benchmark in the Julia and Python notebooks.
"""


from os import system


# Compile the fortran lib_stat source code to object file
path = '../../../src/Ch13_StatisticalDescriptionOfData/student_ttest/lib_stat'
system('gfortran -c ' + path + '/lib_stat.f90')

# Compile the fortran tests source code to object files
system('gfortran -c *.f90')

# Link the objects to create standalone programs that
# later will be called from the python scripts
system('gfortran lib_stat.o test_avevar.o -o fmain_test_avevar')
system('gfortran lib_stat.o test_betai.o -o fmain_test_betai')
system('gfortran lib_stat.o test_gammaln.o -o fmain_test_gammaln')

# Remove unnecessary objects and module
system('rm *.o *.mod')
