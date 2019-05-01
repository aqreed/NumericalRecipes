import numpy as np
from numba import jit


@jit(nopython=True)
def gammaln(xx):
    # Returns the value of ln[gamma(XX)] for X > 0.
    # Full accuracy is obtained for XX > 1.
    cof = np.array([76.18009173, -86.50532033, 24.01409822,
                    -1.231739516, 0.120858003e-2, -0.536382e-5])
    stp = 2.50662827465

    x = xx - 1.0
    tmp = x + 5.5
    tmp = (x + 0.5) * np.log(tmp) - tmp
    ser = 1.0

    for i in range(len(cof)):
        x = x + 1
        ser = ser + cof[i] / x

    gammaln = tmp + np.log(stp * ser)
    return gammaln
