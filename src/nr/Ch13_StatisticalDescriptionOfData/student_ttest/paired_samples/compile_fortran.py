"""
    Script to compile the Fortran files required to serve as
    benchmark in the Julia and Python notebooks.
"""


from os import system, path


# Compile Fortran source code to object file
system('gfortran -c ../../../Ch6_SpecialFunctions/betacf/betacf.f90')
system('gfortran -c ../../../Ch6_SpecialFunctions/gammaln/gammaln.f90')
system('gfortran -c ../../../Ch6_SpecialFunctions/betai/betai.f90')
system('gfortran -c ../../avevar/avevar.f90')

# Compile the Fortran program and speed test source codes to object files,
# then link the objects to create standalone programs
if not path.isfile('fmain_tptest') or not path.isfile('fspeed_tptest'):
    # compile
    system('gfortran -c tptest.f90')
    system('gfortran -c tptest_speedTest.f90')
    # link
    system('gfortran betai.o betacf.o gammaln.o avevar.o tptest.o -o fmain_tptest')
    system('gfortran betai.o betacf.o gammaln.o avevar.o tptest_speedTest.o -o fspeed_tptest')

# Remove unnecessary objects and module
system('rm *.o *.mod')
