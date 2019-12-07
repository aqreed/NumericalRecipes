import numpy as np
import sys
import numericalrecipes as nr


def betai(a, b, x):
    # Returns the incomplete beta function Ix(a, b)
    if ((x < 0) or (x > 1)):
        print('BETAI: bad argument fo x')
        sys.exit()

    # Factor "bt" in front of continued fraction
    if ((x == 0) or (x == 1)):
        # Continued fraction
        if (x < ((a + 1) / (a + b + 2))):
            # ...directly
            return 0
        else:
            # ...after symmetry transformation
            return 1
    else:
        bt = np.exp(nr.gammaln(a + b) - nr.gammaln(a) - nr.gammaln(b) +
                    a * np.log(x) + b * np.log(1 - x))
        # Continued fraction
        if (x < ((a + 1) / (a + b + 2))):
            # ...directly
            return bt * nr.betacf(a, b, x) / a
        else:
            # ...after symmetry transformation
            return 1 - bt * nr.betacf(b, a, 1 - x) / b
