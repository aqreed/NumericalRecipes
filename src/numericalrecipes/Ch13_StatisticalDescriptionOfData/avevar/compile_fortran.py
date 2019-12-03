"""
    Script to compile the Fortran files required to serve
    as benchmark in the Julia and Python notebooks.
"""
from os import system


# Compile the Fortran source code to object files
system('gfortran -c avevar.f90 speed_avevar.f90')

# Link the objects to create the executable
system('gfortran avevar.o speed_avevar.o -o fspeed_avevar')

# Remove unnecessary objects and module
system('rm *.o *.mod')
