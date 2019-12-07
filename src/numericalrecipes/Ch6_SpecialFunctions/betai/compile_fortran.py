"""
    Script to compile the Fortran files required to serve
    as benchmark in the Julia and Python notebooks.
"""
from os import system, chdir, getcwd


# Compile the Fortran tests source code to object files
system('gfortran -c ../betacf/betacf.f90')  # compile betacf
system('gfortran -c ../gammaln/gammaln.f90')  # compile gammaln
system('gfortran -c betai.f90 speed_betai.f90')

# Link the objects to create the executable
system('gfortran betacf.o gammaln.o betai.o speed_betai.o -o fspeed_betai')

# Remove unnecessary objects and module
system('rm *.o *.mod')
