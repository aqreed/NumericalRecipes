"""
    Script to compile the Fortran and C++ files required to
    serve as benchmark in the Julia and Python notebooks.
"""
from os import system, chdir, getcwd

# Fortran
# Compile source code to object files
system('gfortran -c gammaln.f90 speed_gammaln.f90')
# Link the objects to create the executable
system('gfortran gammaln.o speed_gammaln.o -o fspeed_gammaln')
# Remove unnecessary objects and module
system('rm *.o *.mod')

# C++
# Compile an link source code to create executable
system('g++ gammaln.cpp speed_gammaln.cpp -o cppSpeed_gammaln')
