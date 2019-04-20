import numpy as np
import os
import sys


# get current directory and change dir to it
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# add to path the lib paths
sys.path.append(os.path.realpath('../gammaln'))
from gammaln import gammaln

sys.path.append(os.path.realpath('../betacf'))
from betacf import betacf


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
