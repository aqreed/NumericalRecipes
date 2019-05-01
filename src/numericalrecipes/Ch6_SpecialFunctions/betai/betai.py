import numpy as np
import sys
import nr


def betai(a, b, x):
    # Returns the incomplete beta function Ix(a, b)

    if ((x < 0) or (x > 1)):
        print('BETAI: bad argument fo x')
        sys.exit()

    # Factor "bt" in front of continued fraction
    if ((x == 0) or (x == 1)):
        bt = 0
    else:
        bt = np.exp(nr.gammaln(a + b) - nr.gammaln(a) - nr.gammaln(b) +
                    a * np.log(x) + b * np.log(1 - x))

    # Continued fraction
    if (x < ((a + 1) / (a + b + 2))):
        # ...directly
        betai = bt * nr.betacf(a, b, x) / a
        return betai
    else:
        # ...after symmetry transformation
        betai = 1 - bt * nr.betacf(b, a, 1 - x) / b
        return betai
