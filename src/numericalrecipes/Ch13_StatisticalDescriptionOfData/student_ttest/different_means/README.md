### Student's t-test for significantly different means

The Jupyter notebooks compare the algorithm in Julia and Python with the Fortran version. The comparison consists in a simple loop, executing the function a million times. The results show clearly that Julia is faster than Fortran and much faster than Python:

| Languague | Python | Julia | Fortran |
| :---: | :---: | :---: | :---: |
| Time | 20.3 s | 499 ms | 702 ms |
