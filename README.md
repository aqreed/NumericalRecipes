# NumericalRecipes

Is Julia as fast as Fortran, C or C++, and as easy as Python? 

I will try to answer this question using the algorithms found in Press, W. H., Flannery, B. P., Teukolsky, S. A., Vetterling, W. T., 1986, _Numerical Recipes. The Art of Scientific Computing_, Cambridge University Press, 818 p

Each algorithm will have a separated directory containing source code and speed test in the compiled languages (Fortran, C, C++), alongside two Jupyter notebooks to compare Julia and Python scripts time execution against them. The naming criteria is:

- [algorithm].f90
- [algorithm].jl
- [algorithm].py
- [algorithm]_julia.ipynb
- [algorithm]_python.ipynb

Python will be also used for testing and compiling Fortran source code.

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
  julia> import NumericalRecipes
  julia> NumericalRecipes.gammaln(1)
  -3.413624938275461e-11
```
Run tests with:

``` julia
  julia> using Pkg

  julia> Pkg.test("NumericalRecipes")
     Testing NumericalRecipes
   Resolving package versions...
Test Summary: | Pass  Total
test_betai    |    4      4
Test Summary: | Pass  Total
test_gamma    |    2      2
Test Summary: | Pass  Total
test_avevar   |    6      6
   Testing NumericalRecipes tests passed
```
