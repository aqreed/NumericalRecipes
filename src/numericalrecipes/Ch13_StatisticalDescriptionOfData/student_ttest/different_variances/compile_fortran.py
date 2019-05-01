"""
    Script to compile the Fortran files required to serve
    as benchmark in the Julia and Python notebooks.
"""


from os import system, path


# Compile modules Fortran source code to object files
system('gfortran -c ../../../Ch6_SpecialFunctions/betacf/betacf.f90')
system('gfortran -c ../../../Ch6_SpecialFunctions/gammaln/gammaln.f90')
system('gfortran -c ../../../Ch6_SpecialFunctions/betai/betai.f90')
system('gfortran -c ../../avevar/avevar.f90')

# Compile main Fortran program source code and then
# link the objects to create the executable
if not path.isfile('fmain_tutest'):
    # compile
    system('gfortran -c tutest.f90')
    # link
    system('gfortran betai.o betacf.o gammaln.o avevar.o tutest.o -o fmain_tutest')

# Remove unnecessary objects and module
system('rm *.o *.mod')
