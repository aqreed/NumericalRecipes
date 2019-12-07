module mod_betai
   ! Contains the following functions: betai
   use mod_betacf
   use mod_gammaln
   implicit none
   contains

   function betai(a, b, x)
      ! Returns the incomplete beta function Ix(a, b)
      implicit none
      real(8), intent(in)     :: a, b, x
      real(8)                 :: bt, betai

      if ((x < 0.0d0) .or. (x > 1.0d0)) then
         write(*, *) 'BETAI: bad argument for x' 
         stop
      end if

      ! Factor "bt" in front of continued fraction
      if ((x == 0.0d0) .or. (x == 1.0d0)) then
         bt = 0.0d0
      else
         bt = exp(gammaln(a + b) - gammaln(a) - gammaln(b) + &
              a * log(x) + b * log(1.0d0 - x))
      end if

      ! Continued fraction
      if (x < ((a + 1.0d0) / (a + b + 2.0d0))) then
         ! ...directly
         betai = bt * betacf(a, b, x) / a
         return
      else
         ! ...after symmetry transformation
         betai = 1.0d0 - bt * betacf(b, a, 1.0d0 - x) / b
         return
      end if

   end function betai

end module mod_betai