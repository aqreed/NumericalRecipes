"""
    Script to compile the Fortran files required to serve as
    benchmark in the Julia and Python notebooks.
"""


from os import system, path, getcwd, chdir


# get current directory and change dir to it
chdir(getcwd())

# Compile Fortran source code to object file
system('gfortran -c ../../../Ch6_SpecialFunctions/betacf/betacf.f90')
system('gfortran -c ../../../Ch6_SpecialFunctions/gammaln/gammaln.f90')
system('gfortran -c ../../../Ch6_SpecialFunctions/betai/betai.f90')
system('gfortran -c ../../avevar/avevar.f90')

# Compile the Fortran program and speed test source codes to object files,
# then link the objects to create standalone programs
if not path.isfile('fmain_tutest') or not path.isfile('fspeed_tuest'):
    # compile
    system('gfortran -c tutest.f90')
    system('gfortran -c tutest_speedTest.f90')
    # link
    system('gfortran betai.o betacf.o gammaln.o avevar.o tutest.o -o fmain_tutest')
    system('gfortran betai.o betacf.o gammaln.o avevar.o tutest_speedTest.o -o fspeed_tutest')

# Remove unnecessary objects and module
system('rm *.o *.mod')
