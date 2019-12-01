module mod_tptest
   ! Contains the following subroutine: tptest
   implicit none
   contains

   subroutine tptest(data1, n1, data2, n2, t, prob)
      ! Given the arrays "data1" and "data2" of length "n", returns the
      ! Student's "t" for paired data and its significance as "prob". Small
      ! values of "prob" indicates that the arrays have different means.
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

      ! Degrees of freedom
      df = n - 1.0d0
      
      cov = cov / df

      ! Student's t
      t = (ave1 - ave2) / sqrt((var1 + var2 - 2.0d0 * cov) / n)

      ! Significance
      prob = betai(0.5d0 * df, 0.5d0, (df / (df + t**2)))
   end subroutine tptest

end module mod_tptest
