module mod_tptest
    # Contains function(s): tptest

    # Import Julia functions
    include("../../avevar/avevar.jl")
    using .mod_avevar: avevar

    include("../../../Ch6_SpecialFunctions/betai/betai.jl")
    using .mod_betai: betai


    function tptest(data1, data2)
        # Given the arrays "data1" and "data2" of length "n",
        # returns the Student's "t" for paired data and its 
        # significance as "prob".

        # Small values of "prob" indicates that the arrays have
        # different means.

        n1 = length(data1)
        n2 = length(data2)
      
        if (n1 != n2)
            print("Data arrays must have the same size")
        else
            n = n1
        end

        ave1, var1 = avevar(data1)
        ave2, var2 = avevar(data2)

        cov = 0.0
        for i = 1:n
          cov = cov + (data1[i] - ave1) * (data2[i] - ave2)
        end

        df = n - 1.0
        cov = cov / df

        # Student's t
        t = (ave1 - ave2) / sqrt((var1 + var2 - 2.0 * cov) / n)

        # significance
        prob = betai(0.5 * df, 0.5, df/(df + t^2))
        return t, prob
    end

end