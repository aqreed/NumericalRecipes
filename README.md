# NumericalRecipes

Is Julia as fast as Fortran, C or C++, and as easy as Python? 

I will try to answer this question using the algorithms found in Press, W. H., Flannery, B. P., Teukolsky, S. A., Vetterling, W. T., 1986, _Numerical Recipes. The Art of Scientific Computing_, Cambridge University Press, 818 p

#### Python install

Install package `nr` with:

``` console
  $ python setup.py install
```
Then, functions may be called as:

```python
import nr
nr.gammaln(1)
```
Run tests with:

``` console
  $ py.test
```

Each algorithm will have a separated directory containing source code and speed test in the compiled languages (Fortran, C, C++), alongside two Jupyter notebooks to compare Julia and Python scripts time execution against them. The naming criteria is:

- [algorithm].f90
- [algorithm].jl
- [algorithm].py
- [algorithm]_julia.ipynb
- [algorithm]_python.ipynb

Python will be also used for testing and to compile Fortran source code.