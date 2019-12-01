### Student's t-test for paired samples

The Jupyter notebooks compare both Julia and Python versions of the code with the Fortran, C and C++ ones. The comparison consists in a simple loop, executing the function a million times. The results show clearly that Julia is faster than Python:

| Languague | Time |
| - | - |
| Python | 30.4 s |
| Julia | 415 ms |
| Fortran | 598 ms |
| C | TBD |
| C++ | TBD |

The Fortran source code will be compiled along the necessary libs using a Python script (_compile_fortran.py_). This script will be called at the beginning of each notebook.
