module mod_avevar
   ! Contains the following subroutine: avevar
   implicit none
   contains

   subroutine avevar(data, n, ave, var)
      ! Given an array "data" of length "n", returns
      ! its mean "ave" and its variance "var"
      implicit none
      real(8), intent(in)     :: data(n)
      integer, intent(in)     :: n
      real(8), intent(out)    :: ave, var
      integer                 :: i
      real(8)                 :: s

      ave = 0.0d0
      var = 0.0d0

      ! Mean
      do i = 1, n
         ave = ave + data(i)
      end do

      ave = ave / n

      ! Variance (of a sample population)
      do i = 1, n
         s = data(i) - ave
         var = var + s*s         
      end do

      var = var / (n - 1.0d0)
   end subroutine avevar

end module mod_avevar
