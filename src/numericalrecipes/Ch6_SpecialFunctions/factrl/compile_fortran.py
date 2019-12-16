"""
    Script to compile the Fortran files required to serve
    as benchmark in the Julia and Python notebooks.
"""
from os import system, chdir, getcwd


# Compile the Fortran tests source code to object files
system('gfortran -c ../gammaln/gammaln.f90')  # compile gammaln
system('gfortran -c factrl.f90')

# Link the objects to create the executable
system('gfortran gammaln.o factrl.o')

# Remove unnecessary objects and module
system('rm *.o *.mod')
