program main
   ! COMPILATION:
   ! gfortran -c betacf.f90 speed_betacf.f90
   ! gfortran betacf.o speed_betacf.o -o fspeed_betacf
   use mod_betacf
   implicit none
   integer                              :: i, c1, c2, cr
   real(8)                              :: a, b, x, bcf, time_exec

   ! Input data
   a = 2.3
   b = 4
   x = 0.5

   ! Timing of the for loop
   call system_clock(count_rate=cr)
   call system_clock(c1)

   do i = 1, 1000000
      bcf = betacf(a, b, x)
   end do

   call system_clock(c2)

   time_exec = (c2 - c1) / real(cr)

   write(*,*) bcf, time_exec
end program main
