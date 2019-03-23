program test_avevar
   ! COMPILATION:
   ! gfortran -c lib_stat.f90 test_avevar.f90
   ! gfortran lib_stat.o test_avevar.o -o test_avevar
   use lib_stat
   implicit none

   character(len = 100)                :: x
   real(8)                             :: ave, var, y
   integer                             :: i, n
   real(8), dimension(:), allocatable  :: data

   n = iargc()
   ! captures 1st argument, put it as first element of arrat
   call getarg(1, x)
   read(x, '(f10.0)') y
   data = (/y/)

   ! captures the other arguments, completition of the array
   do i = 2, n
      call getarg(i, x)
      read(x, '(f10.0)') y
      data = [data, y]
   end do
   
   call avevar(data, n, ave, var)

   ! output to stdout
   write(*, *) ave, var
end program test_avevar