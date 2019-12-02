"""
    Script to compile the Fortran files required to serve
    as benchmark in the Julia and Python notebooks.
"""
from os import system


# Compile Fortran modules and source code to object files
system('gfortran -c ../../../Ch6_SpecialFunctions/betacf/betacf.f90')
system('gfortran -c ../../../Ch6_SpecialFunctions/gammaln/gammaln.f90')
system('gfortran -c ../../../Ch6_SpecialFunctions/betai/betai.f90')
system('gfortran -c ../../avevar/avevar.f90')
system('gfortran -c tutest.f90 speed_tutest.f90')

# Link the objects to create the executable
system('gfortran betai.o betacf.o gammaln.o avevar.o tutest.o \
	    speed_tutest.o -o fspeed_tutest')

# Remove unnecessary objects and module
system('rm *.o *.mod')
