program test_ttest
   ! COMPILATION:
   ! gfortran -c avevar.f90 betacf.f90 gammaln.f90 betai.f90 ttest.f90 test_ttest.f90
   ! gfortran avevar.o betacf.o gammaln.o betai.o ttest.o test_ttest.0 -o ftest_ttest
   use mod_ttest
   implicit none

   character(len = 100)                :: x
   real(8)                             :: y, t, prob
   integer                             :: i, j, n1, n2
   real(8), dimension(:), allocatable  :: data1, data2


   ! 1st array
   ! get 1st argument, which contains the length
   call getarg(1, x)
   read(x, '(i100)') n1
 
   ! captures the next n1 arguments, containing the array
   allocate(data1(n1))

   j = 1
   do i = 2, n1 + 2
      call getarg(i, x)
      read(x, '(f10.0)') y
      data1(j) = y
      j = j + 1
   end do

   ! 2nd array
   ! gets (n1 + 2)th argument, which contains the length
   call getarg(n1 + 2, x)
   read(x, '(i100)') n2   

   ! captures the next n2 arguments, containing the array
   allocate(data2(n2))

   j = 1
   do i = n1 + 3, n1 + 3 + n2
      call getarg(i, x)
      read(x, '(f10.0)') y
      data2(j) = y
      j = j + 1
   end do

   ! calls the subroutine
   call ttest(data1, n1, data2, n2, t, prob)
   
   ! output to stdout
   write(*, *) t, prob

   deallocate(data1)
   deallocate(data2)

end program test_ttest
