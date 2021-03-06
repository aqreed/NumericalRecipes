# Contains function(s): gammaln


function gammaln(x)
    # Returns the value of ln[gamma(X)] for X > 0.
    # Full accuracy is obtained for X > 1.

    if (x < 0)
        error("GAMALN: bad argument for x")
    end

    cof = [76.18009173, -86.50532033, 24.01409822,
           -1.231739516, 0.120858003e-2, -0.536382e-5]
    stp = 2.50662827465

    x = x - 1.0
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
