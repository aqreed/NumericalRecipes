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

# Compile Fortran program source code
system('gfortran -c ttest.f90 speed_ttest.f90')

# Link the objects to create the executable
system('gfortran betai.o betacf.o gammaln.o avevar.o ttest.o \
        speed_ttest.o -o fspeed_ttest')

# Remove unnecessary objects and module
system('rm *.o *.mod')
