program test_avevar
   ! COMPILATION:
   ! gfortran -c avevar.f90 test_avevar.f90
   ! gfortran avevar.o test_avevar.o -o ftest_avevar

   use mod_avevar
   implicit none

   character(len = 100)                :: x
   real(8)                             :: ave, var, y
   integer                             :: i, n
   real(8), dimension(:), allocatable  :: data

   n = iargc()

   ! captures 1st argument, put it as first element of array
   call getarg(1, x)
   read(x, '(f10.0)') y
   data = (/y/)

   ! captures the other arguments, completition of the array
   do i = 2, n
      call getarg(i, x)
      read(x, '(f10.0)') y
      data = [data, y]
   end do
   
   ! calls the subroutine
   call avevar(data, n, ave, var)

   ! output to stdout
   write(*, *) ave, var
end program test_avevar