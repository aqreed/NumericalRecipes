import numpy as np
import sys
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


def betacf(a, b, x):
    # Continued fraction for incomplete beta function,
    # used by "betai"
    eps = 3.0e-7
    imax = 100

    am, bm, az = 1, 1, 1
    qab = a + b
    qap = a + 1
    qam = a - 1
    bz = 1. - (qab * x) / qap

    # continued fraction evaluation using recurrence
    for m in range(1, imax):
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

        if (abs(az - aold) < eps * abs(az)):
            # print('BETACF: convergence OK')
            break

        if (m == imax):
            print('BETACF: a or b too big, or imax too small')
            sys.exit()

        betacf = az
        return betacf


def betai(a, b, x):
    # Returns the incomplete beta function Ix(a, b)

    if ((x < 0) or (x > 1)):
        print('BETAI: bad argument fo x')
        sys.exit()

    # Factor "bt" in front of continued fraction
    if ((x == 0) or (x == 1)):
        bt = 0
    else:
        bt = np.exp(gammaln(a + b) - gammaln(a) - gammaln(b) +
                    a * np.log(x) + b * np.log(1 - x))

    # Continued fraction
    if (x < ((a + 1) / (a + b + 2))):
        # ...directly
        betai = bt * betacf(a, b, x) / a
        return betai
    else:
        # ...after symmetry transformation
        betai = 1 - bt * betacf(b, a, 1 - x) / b
        return betai
