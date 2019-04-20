"""
    Script to compile the Fortran files required to serve as
    benchmark in the Julia and Python notebooks.
"""


from os import system, path, getcwd, chdir


# get current directory and change dir to it
chdir(getcwd())

# Compile Fortran source code to object file
system('gfortran -c lib_stat.f90 ../../avevar/avevar.f90')

# Compile the Fortran program and speed test source codes to object files,
# then link the objects to create standalone programs
if not path.isfile('fmain_ttest') or not path.isfile('fspeed_ttest'):
    # compile
    system('gfortran -c ../significantly_different_means/ttest.f90')
    system('gfortran -c ../significantly_different_means/ttest_speedTest.f90')
    # link
    system('gfortran lib_stat.o avevar.o ttest.o -o fmain_ttest')
    system('gfortran lib_stat.o avevar.o ttest_speedTest.o -o fspeed_ttest')

if not path.isfile('fmain_tutest') or not path.isfile('fspeed_tuest'):
    # compile
    system('gfortran -c ../significantly_different_variances/tutest.f90')
    system('gfortran -c ../significantly_different_variances/tutest_speedTest.f90')
    # link
    system('gfortran lib_stat.o avevar.o tutest.o -o fmain_tutest')
    system('gfortran lib_stat.o avevar.o tutest_speedTest.o -o fspeed_tutest')

if not path.isfile('fmain_tptest') or not path.isfile('fspeed_tptest'):
    # compile
    system('gfortran -c ../paired_samples/tptest.f90')
    system('gfortran -c ../paired_samples/tptest_speedTest.f90')
    # link
    system('gfortran lib_stat.o avevar.o tptest.o -o fmain_tptest')
    system('gfortran lib_stat.o avevar.o tptest_speedTest.o -o fspeed_tptest')

# Remove unnecessary objects and module
system('rm *.o *.mod')
