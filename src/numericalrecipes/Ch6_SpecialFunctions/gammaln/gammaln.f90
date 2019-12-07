module mod_gammaln
   ! Contains the following functions: gammaln
   implicit none
   contains

   function gammaln(xx)
      ! Returns the value of ln[gamma(XX)] for X > 0. Full accuracy is 
      ! obtained for XX > 1. 
      implicit none
      real(8), intent(in)              :: xx
      real(8)                          :: gammaln
      real(8), parameter, dimension(6) :: cof = (/76.18009173d0, -86.50532033d0, &
                                                  24.01409822d0, -1.231739516d0, &
                                                  .120858003d-2, -.536382d-5/)
      real(8), parameter               :: stp = 2.50662827465d0
      real(8)                          :: x, tmp, ser
      integer                          :: i

      x = xx - 1.0d0
      tmp = x + 5.5d0
      tmp = (x + .5) * log(tmp) - tmp
      ser = 1.0d0

      do i = 1, 6
         x = x + 1.0d0
         ser = ser + cof(i) / x
      end do 

      gammaln = tmp + log(stp * ser)
   end function gammaln

end module mod_gammaln