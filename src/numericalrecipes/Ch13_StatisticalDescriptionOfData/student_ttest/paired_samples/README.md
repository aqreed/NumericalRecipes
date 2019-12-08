### Student's t-test for paired samples

The Jupyter notebooks compare the algorithm in Julia and Python with the Fortran version. The comparison consists in a simple loop, executing the function a million times. The results show clearly that Julia is faster than Fortran and much faster than Python:

| Languague | Python | Julia | Fortran |
| :---: | :---: | :---: | :---: |
| Time | 30.4 s | 415 ms | 598 ms |
