module mod_tutest
   ! Contains the following subroutine: tutest
   implicit none
   contains

   subroutine tutest(data1, n1, data2, n2, t, prob)
      ! Given the arrays "data1" and "data2" of lengths "n1" and "n2", returns
      ! the Student's "t" and its significance as "prob".
      ! Data are assumed to be drawn from populations with unequal variances.
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

      ! Degrees of freedom
      df = (var1 / n1 + var2 / n2)**2 / ((var1 / n1)**2 / (n1 - 1) + &
                                         (var2 / n2)**2 / (n2 - 1))

      ! Student's t
      t = (ave1 - ave2) / sqrt(var1 / n1 + var2 / n2)

      ! Significance
      prob = betai(0.5d0 * df, 0.5d0, df / (df + t**2))
   end subroutine tutest

end module mod_tutest
