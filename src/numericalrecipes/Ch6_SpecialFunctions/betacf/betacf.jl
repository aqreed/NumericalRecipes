module mod_betacf
    # Contains function(s): betacf

    function betacf(a, b, x)
        # Continued fraction for incomplete beta function, 
        # used by "betai"  
        eps = 3.0e-7
        imax = 100

        am, bm, az = 1, 1, 1
        qab = a + b
        qap = a + 1
        qam = a - 1
        bz = 1 - (qab * x) / qap

        # continued fraction evaluation using recurrence
        for m = 1:imax
            em = m
            tem = em + em
            d = (em * (b - m) * x) / ((qam + tem) * (a + tem))
            ap = az + d * am
            bp = bz + d * bm
            d = -((a + em) * (qab + em) * x) / ((a + tem) * (qap + tem))
            app = ap + d * az
            bpp = bp + d * bz
            aold = az
            am = ap / bpp
            bm = bp / bpp
            az = app / bpp
            bz = 1.0

            if (abs(az - aold) < eps * abs(az))
                # print('BETACF: convergence OK')
                break
            end

            if (m == imax)
                error("BETACF: a or b too big, or imax too small")
            end
        end

        betacf = az
        return betacf
    end

end