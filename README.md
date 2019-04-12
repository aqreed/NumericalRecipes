# NumericalRecipes

Is Julia fast as Fortran, and easy as Python? 

I will try to answer this question using the equations and algorithms found in Press, W. H., Flannery, B. P., Teukolsky, S. A., Vetterling, W. T., 1986, _Numerical Recipes. The Art of Scientific Computing_, Cambridge University Press, 818 p

Each algorithm will be put in a separated directory one level up, where two Jupyter notebooks will compare Julia and Python scripts time execution against Fortran's. The naming criteria is:

- [function].f90
- [function]_julia_vs_fortran.ipynb
- [function]_python_vs_fortran.ipynb

Common functions and subroutines will be placed in a folder named lib_[topic], one file for each languague. Python will be also used for testing and to compile Fortran source code.