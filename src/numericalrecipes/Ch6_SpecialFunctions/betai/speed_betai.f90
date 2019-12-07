program main
   ! COMPILATION:
   ! gfortran -c betacf.f90 gammaln.f90 betai.f90 speed_betai.f90
   ! gfortran betacf.o gammaln.o betai.o speed_betai.o -o fspeed_betai
   use mod_betai
   implicit none
   real(8)                 :: a, b, x, beta_i, time_exec
   integer                 :: i, c1, c2, cr

   ! Input data
   a = 0.3
   b = 2
   x = 0.25

   ! Timing of the for loop
   call system_clock(count_rate=cr)
   call system_clock(c1)

   do i = 1, 1000000
      beta_i = betai(a, b, x)
   end do

   call system_clock(c2)

   time_exec = (c2 - c1) / real(cr)

   write(*,*) beta_i, time_exec
end program main
