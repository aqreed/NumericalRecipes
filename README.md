# NumericalRecipes

Is Julia fast as Fortran, and easy as Python? 

I will try to answer this question using the equations and algorithms found in Press, W. H., Flannery, B. P., Teukolsky, S. A., Vetterling, W. T., 1986, _Numerical Recipes. The Art of Scientific Computing_, Cambridge University Press, 818 p

Each Fortran algorithm will be put in a separated directory alongside a speed test, and two Jupyter notebooks will compare Julia and Python scripts time execution against Fortran's. The naming criteria is:

- [algorithm].f90
- [algorithm]_speedTest.f90
- [algorithm]_julia_vs_fortran.ipynb
- [algorithm]_python_vs_fortran.ipynb
 
Common functions and subroutines are placed in a folder one level up named lib_[topic], one file for each languague. The naming criteria for these files is:

- lib_[topic].f90
- lib_[topic].jl
- lib_[topic].py

Python will be also used for testing and to compile Fortran source code.