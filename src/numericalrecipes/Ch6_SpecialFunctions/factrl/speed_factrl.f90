program main
   ! COMPILATION:
   ! gfortran -c factrl.f90 speed_factrl.f90
   ! gfortran factrl.o speed_factrl.o -o fspeed_factrl
   use mod_factrl
   implicit none
   real(8)                 :: fact, time_exec
   integer                 :: n, i, c1, c2, cr

   ! Input data
   n = 5

   ! Timing of the for loop
   call system_clock(count_rate=cr)
   call system_clock(c1)

   do i = 1, 1000000
      fact = factrl(n)
   end do

   call system_clock(c2)

   time_exec = (c2 - c1) / real(cr)

   write(*,*) fact, time_exec
end program main
