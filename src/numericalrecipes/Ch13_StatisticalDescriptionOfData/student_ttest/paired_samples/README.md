### Student's t-test for paired samples

The Jupyter notebooks compare both Julia and Python versions of the code with the Fortran, C and C++ ones. The results show clearly that Julia is faster than Python when we benchmark both of them to these compiled languages:

| |Python|Julia|
|-|------|-----|
|Fortran| ~33.3 times slower| ~1.5 times faster|
|C| TBD| TBD|
|C++| TBD| TBD|

_Note:_ this must be read as _"in a Python script, using a Python function is 33.3 times slower than calling Fortran executable code from the same script"_

The Fortran source code will be compiled along the necessary libs using a Python script (_compile_fortran.py_). This script will be called at the beginning of each notebook.