module mod_gammaln
    # Contains function(s): gammaln

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
            ser = ser + cof[i] / x
        end

        gammaln = tmp + log(stp * ser)
        return gammaln
    end

end