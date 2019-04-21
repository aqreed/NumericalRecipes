program test_gammaln
   ! COMPILATION:
   ! gfortran -c gammaln.f90 test_gammaln.f90
   ! gfortran gammaln.o test_gammaln.o -o ftest_gammaln

   use mod_gammaln
   implicit none

   character(len = 15)   :: x
   real(8)               :: y

   ! captures argument
   call getarg(1, x)

   ! convert to float
   read(x, '(f10.0)') y

   ! output to stdout
   write(*, *) gammaln(y)
end program test_gammaln