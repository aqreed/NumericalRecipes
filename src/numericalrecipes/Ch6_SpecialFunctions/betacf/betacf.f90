module mod_betacf
   ! Contains the following functions: betacf
   implicit none
   contains

   function betacf(a, b, x)
      ! Continued fraction for incomplete beta function, used by "betai"  
      implicit none
      real(8), intent(in)     :: a, b, x
      real(8), parameter      :: eps = 3.0d-7
      integer, parameter      :: imax = 100
      real(8)                 :: am, bm, az, qab, qap, &
                                 qam, bz, em, tem, d, ap, &
                                 bp, app, bpp, aold, betacf
      integer                 :: m

      am = 1.0d0
      bm = 1.0d0
      az = 1.0d0
      qab = a + b
      qap = a + 1.0d0
      qam = a - 1.0d0
      bz = 1.0d0 - (qab * x) / qap

      ! Continued fraction evaluation using recurrence
      do m = 1, imax
         em = m
         tem = em + em
         d = em * (b - m) * x / ((qam + tem) * (a + tem))
         ap = az + d * am
         bp = bz + d * bm
         d = -((a + em) * (qab + em) * x) / ((a + tem) * (qap + tem))
         app = ap + d * az
         bpp = bp + d * bz
         aold = az
         am = ap / bpp
         bm = bp / bpp
         az = app / bpp
         bz = 1.0d0

         if (abs(az - aold) < eps * abs(az)) then
            !write(*, *) 'BETACF: convergence OK'
            exit
         end if

         if (m == imax) then
            write(*, *) 'BETACF: a or b too big, or imax too small'
            stop
         end if
      end do

      betacf = az
   end function betacf

end module mod_betacf
