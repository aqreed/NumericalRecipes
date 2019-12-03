"""
    Script to compile the Fortran files required to serve
    as benchmark in the Julia and Python notebooks.
"""
from os import system


# Compile the Fortran source code to object files
system('gfortran -c betacf.f90 speed_betacf.f90')

# Link the objects to create the executable
system('gfortran betacf.o speed_betacf.o -o fspeed_betacf')

# Remove unnecessary objects and module
system('rm *.o *.mod')
