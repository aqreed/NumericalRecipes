### Gammaln - Logarithm of the gamma function

The Jupyter notebooks compare the algorithm in Julia and Python with the Fortran version. The comparison consists in a simple loop, executing the function a million times. The results show clearly that Julia is faster than Fortran and much faster than Python:

| Languague | Python | Julia | Fortran |
| :---: | :---: | :---: | :---: |
| Time | 529 ms | 98.72 ms | 117 ms |
