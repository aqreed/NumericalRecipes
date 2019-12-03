program main
   ! COMPILATION:
   ! gfortran -c avevar.f90 speed_avevar.f90
   ! gfortran avevar.o speed_avevar.o -o fspeed_avevar
   use mod_avevar
   implicit none
   integer                              :: n, i, c1, c2, cr
   real(8), dimension(:), allocatable   :: data
   real(8)                              :: ave, var, time_exec

   ! Input data
   data = (/1.0d0, 3.0d0, 5.0d0, 6.0d0, 7.0d0, 8.0d0, 9.0d0/)
   n = size(data)

   ! Timing of the for loop
   call system_clock(count_rate=cr)
   call system_clock(c1)

   do i = 1, 1000000
      call avevar(data, n, ave, var)
   end do

   call system_clock(c2)

   time_exec = (c2 - c1) / real(cr)

   write(*,*) ave, var, time_exec
end program main
