# NumericalRecipes

[![Build Status](https://travis-ci.com/aqreed/NumericalRecipes.svg?branch=new_package_name)](https://travis-ci.com/aqreed/NumericalRecipes)
[![codecov.io](https://codecov.io/gh/aqreed/NumericalRecipes/branch/new_package_name/graph/badge.svg)](https://codecov.io/gh/aqreed/NumericalRecipes/branch/new_package_name)

|  |  |
| ------ | ------ |
| Description | Julia vs Python vs Fortran comparison using "Numerical Recipes" |
| Author | aqreed <aqreed@protonmail.com> |
| Version | 0.0.1 |
| Python Version | 3.6 |
| Python Requires | Numpy, Numba, Scipy |
| Julia Version | 1.1 |
| Julia Requires | HypothesisTests, Test |

Is Julia as fast as Fortran, C or C++, and as easy as Python? 

I will try to answer this question using the algorithms found in Press, W. H., Flannery, B. P., Teukolsky, S. A., Vetterling, W. T., 1986, _Numerical Recipes. The Art of Scientific Computing_, Cambridge University Press, 818 p

Each algorithm will have a separated directory containing source code and speed test in the compiled languages (Fortran, C, C++), Julia and Python. The naming criteria is:

- [algorithm].f90
- speed_[algorithm].f90
- [algorithm].jl
- [algorithm].py

Also two Jupyter notebooks will compare Julia and Python scripts time execution against the compiled languages:

- [algorithm]_julia.ipynb
- [algorithm]_python.ipynb

Python will be also used for testing and compiling Fortran source code:

- compile_Fortran.py

And finally the results will be summarized in a readme file.

#### Python install and tests

Install package `numericalrecipes` (from the top directory) in development mode with:

``` console
  $ pip install -e .
```
Then, functions may be called as:

```python
import numericalrecipes as nr
nr.gammaln(1)
```
Run tests (from the top directory) with:

``` console
  $ pytest
```

#### Julia install and tests

To install package `NumericalRecipes` open the Julia console:

``` console
  $ julia
```

Press "]" to enter `pkg` mode. Then activate the pkg:

``` julia
  (v1.1) pkg> activate .
  (NumericalRecipes) pkg>

```

Then, return to normal mode to import functions, which may be called as:

```julia
import NumericalRecipes
NumericalRecipes.gammaln(1)
```
Run tests with:

``` julia
  julia> using Pkg

  julia> Pkg.test("NumericalRecipes")
```
