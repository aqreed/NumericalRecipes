### Student's t-test for significantly different variances

The Jupyter notebooks compare both Julia and Python versions of the code with the Fortran, C and C++ ones. The results show clearly that Julia is faster than Python when we benchmark both of them to these compiled languages:

| |Python|Julia|
|-|------|-----|
|Fortran| ~2.9 times slower| ~4 times faster|
|C| TBD| TBD|
|C++| TBD| TBD|

_Note:_ this must be read as _"in a Python script, using a Python function is 2.9 times slower than calling Fortran executable code from the same script"_

The Fortran source code will be compiled along the necessary libs using a Python script (_compile_fortran.py_) placed in the lib folder one level up (_lib_stat_). This script will be called at the beginning of each notebook.