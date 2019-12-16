program test_factrl
   ! COMPILATION:
   ! gfortran -c gammaln.f90 factrl.f90 test_factrl.f90
   ! gfortran gammaln.o factrl.o test_factrl.o -o ftest_factrl
   use mod_factrl
   implicit none
   character(len = 15)   :: x
   integer               :: y

   ! Captures argument
   call getarg(1, x)

   ! Convert to integer
   read(x, '(i4)') y

   ! Output to stdout
   write(*, *) factrl(y)
end program test_factrl
