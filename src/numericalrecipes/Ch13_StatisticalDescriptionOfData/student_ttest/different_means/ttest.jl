# Contains function(s): ttest


function ttest(data1, data2)
    # Given the arrays "data1" and "data2", returns the
    # Student's "t" and its significance as "prob".
    # Data are assumed to be drawn from populations with
    # the same true variance.

    # Small values of "prob" indicates that the arrays
    # have different means.
    n1 = length(data1)
    n2 = length(data2)

    ave1, var1 = avevar(data1)
    ave2, var2 = avevar(data2)

    # Degrees of freedom
    df = n1 + n2 - 2
    
    # Pooled variance
    var = ((n1 - 1) * var1 + (n2 - 1) * var2) / df
    
    # Student's t
    t = (ave1 - ave2) / sqrt(var * (1 / n1 + 1 / n2))
    
    # Significance
    prob = betai(0.5 * df, 0.5, df / (df + t^2))

    return t, prob
end
