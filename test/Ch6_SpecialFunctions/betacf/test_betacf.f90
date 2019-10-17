program test_betacf
   ! COMPILATION:
   ! gfortran -c betacf.f90 test_betacf.f90
   ! gfortran betacf.o test_betacf.o -o ftest_betacf
   use mod_betacf
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
   write(*, *) betacf(a, b, x_)
end program test_betacf