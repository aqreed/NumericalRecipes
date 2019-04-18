# NumericalRecipes

Is Julia as fast as Fortran, C or C++, and as easy as Python? 

I will try to answer this question using the algorithms found in Press, W. H., Flannery, B. P., Teukolsky, S. A., Vetterling, W. T., 1986, _Numerical Recipes. The Art of Scientific Computing_, Cambridge University Press, 818 p

Each algorithm will have a separated directory containing source code and speed test in the compiled languages (Fortran, C, C++), alongside two Jupyter notebooks to compare Julia and Python scripts time execution against them. The naming criteria is:

- [algorithm].f90
- [algorithm]_speedTest.f90
- [algorithm]_julia.ipynb
- [algorithm]_python.ipynb
 
Common functions and subroutines are placed in a folder one level up named lib_[topic], one file for each languague. The naming criteria for these files is:

- lib_[topic].f90
- lib_[topic].jl
- lib_[topic].py

Python will be also used for testing and to compile Fortran source code.