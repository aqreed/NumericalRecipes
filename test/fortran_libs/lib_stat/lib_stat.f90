module lib_stat
   ! Contains the following functions: gammaln, betacf, betai
   ! Contains the following subroutine: avevar
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

   function betacf(a, b, x)
      ! continued fraction for incomplete beta function, used by "betai"  
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
      
      !continued fraction evaluation using recurrence
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
         am = ap / app
         bm = bp / bpp
         az = app / bpp
         bz = 1.0d0

         if (abs(az - aold) < eps * abs(az)) then
            write(*, *) 'BETACF: convergence OK'
            exit
         end if

         if (m == imax) then
            write(*, *) 'BETACF: a or b too big, or imax too small'
            stop
         end if
      end do

      betacf = az
   end function betacf


   function betai(a, b, x)
      ! Returns the incomplete beta function Ix(a, b)
      implicit none
      real(8), intent(in)     :: a, b, x
      real(8)                 :: bt, betai
      
      if ((x < 0.0d0) .or. (x > 1.0d0)) then
         write(*, *) 'BETAI: bad argument fo x' 
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
end module lib_stat