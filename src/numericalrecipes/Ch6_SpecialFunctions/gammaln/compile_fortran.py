"""
    Script to compile the Fortran files required to serve
    as benchmark in the Julia and Python notebooks.
"""
from os import system, chdir, getcwd


# Compile the Fortran tests source code to object files
system('gfortran -c gammaln.f90 speed_gammaln.f90')

# Link the objects to create the executable
system('gfortran gammaln.o speed_gammaln.o -o fspeed_gammaln')

# Remove unnecessary objects and module
system('rm *.o *.mod')
