program test_betai
   ! COMPILATION:
   ! gfortran -c betacf.f90 gammaln.f90 betai.f90 test_betai.f90
   ! gfortran betacf.o gammaln.o betai.o test_betai.o -o ftest_betai
   use mod_betai
   implicit none

   character(len = 100)                :: x
   real(8)                             :: a, b, x_
   integer                             :: i

   ! captures 1st argument
   call getarg(1, x)
   read(x, '(f10.0)') a

   call getarg(2, x)
   read(x, '(f10.0)') b

   call getarg(3, x)
   read(x, '(f10.0)') x_
  
   ! calls the function
   write(*, *) betai(a, b, x_)
end program test_betai