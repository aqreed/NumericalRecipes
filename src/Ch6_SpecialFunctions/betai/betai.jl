module mod_betai
    # Contains function(s): betai

    # Import Julia functions
    include("../gammaln/gammaln.jl")
    using .mod_gammaln: gammaln

    include("../betacf/betacf.jl")
    using .mod_betacf: betacf


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