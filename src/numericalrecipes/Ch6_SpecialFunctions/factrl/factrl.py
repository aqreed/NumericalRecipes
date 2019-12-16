# Contains function(s): factrl
import numpy as np
import numericalrecipes as nr


def factrl(n):
    # Returns the factorial, calculated recursively for the first
    # 33 values, then using the gammaln function
    A = np.empty(33)
    ntop = 0
    A[0] = 1.0

    if (n < 0):
        print("Can not calculate negative factorial")
    elif (n <= ntop):
        factrl = A[n]
    elif (n <= 32):
        for j in range(ntop, n):
            A[j + 1] = (j + 1) * A[j]

        ntop = n
        factrl = A[n]
    else:
        factrl = np.exp(nr.gammaln(n + 1.0))

    return factrl
