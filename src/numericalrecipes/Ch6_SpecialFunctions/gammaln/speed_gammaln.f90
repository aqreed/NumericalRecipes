program main
   ! COMPILATION:
   ! gfortran -c gammaln.f90 speed_gammaln.f90
   ! gfortran gammaln.o speed_gammaln.o -o fspeed_gammaln
   use mod_gammaln
   implicit none
   real(8)                 :: x, gl, time_exec
   integer                 :: i, c1, c2, cr

   ! Input data
   x = 0.25

   ! Timing of the for loop
   call system_clock(count_rate=cr)
   call system_clock(c1)

   do i = 1, 1000000
      gl = gammaln(x)
   end do

   call system_clock(c2)

   time_exec = (c2 - c1) / real(cr)

   write(*,*) gl, time_exec
end program main
