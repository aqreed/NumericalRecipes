program main
   ! COMPILATION:
   ! gfortran -c betacf.f90 gammaln.f90 betai.f90 ttest.f90
   ! gfortran betacf.o gammaln.o betai.o ttest.o -o fmain_ttest
   use mod_ttest
   implicit none
   integer                              :: n1, n2, i, c1, c2, cr
   real(8), dimension(:), allocatable   :: data1, data2
   real(8)                              :: t, prob, time_exec

   ! Input data
   data1 = (/1.0d0, 2.0d0, 3.0d0, 4.0d0, &
             5.0d0, 6.0d0, 7.0d0, 8.0d0, 9.0d0/)
   n1 = size(data1)

   data2 = (/1.1d0, 2.0d0, 3.0d0, 4.0d0, &
             5.0d0, 6.0d0, 7.0d0, 8.0d0, 9.0d0/)
   n2 = size(data2)

   ! Timing of the for loop
   call system_clock(count_rate=cr)
   call system_clock(c1)
   
   do i = 1, 1000000
      call ttest(data1, n1, data2, n2, t, prob)
   end do

   call system_clock(c2)
   
   time_exec = (c2 - c1) / real(cr)

   write(*,*) t, prob, time_exec
end program main
