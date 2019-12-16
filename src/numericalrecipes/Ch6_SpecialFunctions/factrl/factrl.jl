# Contains function(s): factrl


function factrl(n)
    # Returns the factorial, calculated recursively for the first
    # 33 values, then using the gammaln function
    A = Array{Float64}(undef, 33)
    ntop = 0
    A[1] = 1.0
    
    if (n < 0)
        error("Can not calculate negative factorial")
    elseif (n <= ntop)
        factrl = A[n + 1]
    elseif (n <= 32)
        for j = ntop + 1:n
            A[j + 1] = j * A[j]
        end
        ntop = n
        factrl = A[n + 1]
    else
        factrl = exp(gammaln(n + 1.0))
    end

    return factrl
end
