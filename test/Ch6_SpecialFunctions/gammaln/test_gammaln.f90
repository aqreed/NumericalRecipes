program test_gammaln
   ! COMPILATION:
   ! gfortran -c gammaln.f90 test_gammaln.f90
   ! gfortran gammaln.o test_gammaln.o -o ftest_gammaln
   use mod_gammaln
   implicit none
   character(len = 15)   :: x
   real(8)               :: y

   ! Captures argument
   call getarg(1, x)

   ! Convert to float
   read(x, '(f10.0)') y

   ! Output to stdout
   write(*, *) gammaln(y)
end program test_gammaln