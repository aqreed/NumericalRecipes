module lib_stat
    # Contains functions: avevar, gammaln, betacf, betai

    function avevar(data)
        # Given an array "data" of length "n", returns
        # its mean "ave" and its variance "var"
        n = length(data)
        ave = 0
        var = 0
        
        # Mean
        for i = 1:n
            ave =  ave + data[i]
        end
        
        ave = ave / n
        
        # Variance (of a sample population)
        for i = 1:n
            s = data[i] - ave
            var =  var + s^2
        end
            
        var = var / (n - 1)
        
        return ave, var
    end


    function gammaln(xx)
        # Returns the value of ln[gamma(XX)] for X > 0. 
        # Full accuracy is obtained for XX > 1. 
        cof = [76.18009173, -86.50532033, 24.01409822, 
               -1.231739516, 0.120858003e-2, -0.536382e-5]
        stp = 2.50662827465
        
        x = xx - 1.0
        tmp = x + 5.5
        tmp = (x + 0.5) * log(tmp) - tmp
        ser = 1.0

        for i = 1:length(cof)
            x = x + 1
            ser = ser + cof[i] / (x)
        end

        gammaln = tmp + log(stp * ser)
        return gammaln
    end


    function betacf(a, b, x)
        # Continued fraction for incomplete beta function, 
        # used by "betai"  
        eps = 3.0e-7
        imax = 100

        am = 1
        bm = 1
        az = 1
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


    function betai(a, b, x)
        # Returns the incomplete beta function Ix(a, b)

        if ((x < 0) || (x > 1))
            error("BETAI: bad argument for x")
        end

        # Factor "bt" in front of continued fraction
        if ((x == 0 ) || (x == 1))
            bt = 0
        else
            bt = exp(gammaln(a + b) - gammaln(a) - gammaln(b) + 
                     a * log(x) + b * log(1 - x))
        end
        
        # Continued fraction
        if (x < ((a + 1) / (a + b + 2)))
            # ...directly
            betai = bt * betacf(a, b, x) / a
            return betai
        else
            # ...after symmetry transformation
            betai = 1 - bt * betacf(b, a, 1 - x) / b
            return betai
        end
    end

end