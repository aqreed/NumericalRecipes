"""
    Script to compile the fortran files required to serve as
    benchmark in the Julia and Python notebooks.
"""


from os import system, path, chdir


# get current directory and change dir to it (thanks StackOverflow!)
abspath = path.abspath(__file__)
dname = path.dirname(abspath)
chdir(dname)

# Compile the fortran lib_stat source code to object file
system('gfortran -c lib_stat.f90')

# Compile the fortran tests source code to object files, then link
# the objects to create standalone programs
if not path.isfile('fmain_ttest'):
    system('gfortran -c ../significantly_different_means/ttest.f90')
    system('gfortran lib_stat.o ttest.o -o fmain_ttest')

if not path.isfile('fmain_tutest'):
    system('gfortran -c ../significantly_different_variances/tutest.f90')
    system('gfortran lib_stat.o tutest.o -o fmain_tutest')

if not path.isfile('fmain_tptest'):
    system('gfortran -c ../paired_samples/tptest.f90')
    system('gfortran lib_stat.o tptest.o -o fmain_tptest')

# Remove unnecessary objects and module
system('rm *.o *.mod')
