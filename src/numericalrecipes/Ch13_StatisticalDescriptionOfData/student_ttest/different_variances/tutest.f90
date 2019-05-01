subroutine tutest(data1, n1, data2, n2, t, prob)
   ! Given the arrays "data1" and "data2" of lengths "n1" and "n2",
   ! returns the Student's "t" and its significance as "prob".
   ! Data are assumed to be drawn from populations with unequal
   ! variances.
   ! Small values of "prob" indicates that the arrays have different means.
   
   use mod_betai
   use mod_avevar
   implicit none
   real(8), intent(in)                  :: data1(n1), data2(n2)
   integer, intent(in)                  :: n1, n2
   real(8)                              :: ave1, var1, ave2, var2, &
                                           df, var, t, prob


   call avevar(data1, n1, ave1, var1)
   call avevar(data2, n2, ave2, var2)

   ! Student's t
   t = (ave1 - ave2) / sqrt(var1/n1 + var2/n2)

   df = (var1/n1 + var2/n2)**2 / ((var1/n1)**2 / (n1 - 1) + (var2/n2)**2 / (n2 - 1))
   ! significance
   prob = betai(0.5d0 * df, 0.5d0, df/(df + t**2))
end subroutine tutest


program main
   ! COMPILATION:
   ! gfortran -c betacf.f90 gammaln.f90 betai.f90 tutest.f90
   ! gfortran betacf.o gammaln.o betai.o tutest.o -o fmain_tutest
   ! EXECUTION:
   ! ./fmain_tutest
   
   implicit none
   integer                              :: n1, n2, i, c1, c2, cr
   real(8), dimension(:), allocatable   :: data1, data2
   real(8)                              :: t, prob, time_exec
                                        

   ! input data
   data1 = (/1.0d0, 2.0d0, 3.0d0, 4.0d0, &
             5.0d0, 6.0d0, 7.0d0, 8.0d0, 9.0d0/)
   n1 = size(data1)

   data2 = (/1.1d0, 2.0d0, 3.0d0, 4.0d0, &
             5.0d0, 6.0d0, 7.0d0, 8.0d0, 9.0d0/)
   n2 = size(data2)

   ! timing of the for loop
   call system_clock(count_rate=cr)
   call system_clock(c1)
   
   do i = 1, 1000000
      call tutest(data1, n1, data2, n2, t, prob)
   end do

   call system_clock(c2)
   
   time_exec = (c2 - c1) / real(cr)

   write(*,*) t, prob, time_exec
end program main
