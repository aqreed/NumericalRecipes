subroutine tptest(data1, n1, data2, n2, t, prob)
   ! Given the arrays "data1" and "data2" of length "n", returns
   ! the Student's "t" for paired data and its significance as "prob".
   ! Small values of "prob" indicates that the arrays have different
   ! means.
   
   use mod_betai
   use mod_avevar
   implicit none
   real(8), intent(in)                  :: data1(n1), data2(n2)
   integer, intent(in)                  :: n1, n2
   integer                              :: n, i
   real(8)                              :: ave1, var1, ave2, var2, &
                                           df, t, prob, cov


   if (n1 /= n2) then
      write(*, *) "Data arrays must have the same size"
      stop
   else
      n = n1
   end if

   call avevar(data1, n1, ave1, var1)
   call avevar(data2, n2, ave2, var2)
    
   cov = 0.0d0
   do i = 1, n
      cov = cov + (data1(i) - ave1) * (data2(i) - ave2)
   end do

   df = n - 1.0d0
   cov = cov / df
   
   ! Student's t
   t = (ave1 - ave2) / sqrt((var1 + var2 - 2.0d0 * cov) / n)

   ! significance
   prob = betai(0.5d0 * df, 0.5d0, (df/(df + t**2)))
end subroutine tptest


program main
   ! COMPILATION:
   ! gfortran -c betacf.f90 gammaln.f90 betai.f90 tptest.f90
   ! gfortran betacf.o gammaln.o betai.o tptest.o -o fmain_tptest
   ! EXECUTION:
   ! ./fmain_tptest

   implicit none
   integer                              :: n1, n2, i, c1, c2, cr
   real(8), dimension(:), allocatable   :: data1, data2
   real(8)                              :: t, prob, time_exec


   ! input data
   data1 = (/70.0d0, 71.0d0, 72.0d0, 73.0d0, 70.5d0/)
   n1 = size(data1)

   data2 = (/70.15d0, 71.05d0, 71.95d0, 72.85d0, 70.45d0/)
   n2 = size(data2)

   ! timing of the for loop
   call system_clock(count_rate=cr)
   call system_clock(c1)

   do i = 1, 1000000
      call tptest(data1, n1, data2, n2, t, prob)
   end do

   call system_clock(c2)
   
   time_exec = (c2 - c1) / real(cr)

   write(*,*) t, prob, time_exec
end program main