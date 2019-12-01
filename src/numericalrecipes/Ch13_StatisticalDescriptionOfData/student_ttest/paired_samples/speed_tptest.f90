program main
   ! COMPILATION:
   ! gfortran -c betacf.f90 gammaln.f90 betai.f90 tptest.f90 speed_tptest.f90
   ! gfortran betacf.o gammaln.o betai.o tptest.o speed_tptest.o -o fspeed_tptest
   use mod_tptest
   implicit none
   integer                              :: n1, n2, i, c1, c2, cr
   real(8), dimension(:), allocatable   :: data1, data2
   real(8)                              :: t, prob, time_exec

   ! Input data
   data1 = (/70.0d0, 71.0d0, 72.0d0, 73.0d0, 70.5d0/) 
   n1 = size(data1)  

   data2 = (/70.15d0, 71.05d0, 71.95d0, 72.85d0, 70.45d0/)  
   n2 = size(data2)

   ! Timing of the for loop
   call system_clock(count_rate=cr)
   call system_clock(c1)
   
   do i = 1, 1000000
      call tptest(data1, n1, data2, n2, t, prob)
   end do

   call system_clock(c2)
   
   time_exec = (c2 - c1) / real(cr)

   write(*,*) t, prob, time_exec
end program main
