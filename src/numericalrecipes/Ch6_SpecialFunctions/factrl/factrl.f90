module mod_factrl
    ! Contains the following functions: factrl
    use mod_gammaln
    implicit none
    contains

    function factrl(n)
        ! Returns the factorial, calculated recursively for the first
        ! 33 values, then using the gammaln function
        implicit none
        integer, intent(in)        :: n
        integer                    :: j, ntop
        real(8)                    :: factrl
        real(8), dimension(33)     :: A

        ntop = 0
        A(1) = 1.0d0

        if (n < 0) then
            write(*, *) "ERROR: can not calculate negative factorial"
            stop
        else if (n <= ntop) then
            factrl = A(n + 1)
        else if (n <= 32) then
            do j = ntop + 1, n
                A(j + 1) = j * A(j)
            end do
            ntop = n
            factrl = A(n + 1)
        else
            factrl = exp(gammaln(n + 1.0d0))
        end if
   end function factrl

end module mod_factrl


program main
   use mod_factrl
   implicit none
   real(8) :: a
   a = factrl(170)
   write(*, *) a
end program main
