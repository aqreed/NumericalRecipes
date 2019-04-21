import numpy as np
import os
import sys


sys.path.append(os.path.realpath('../../avevar'))
from avevar import avevar

sys.path.append(os.path.realpath('../../../Ch6_SpecialFunctions/betai'))
from betai import betai


def tutest(data1, data2):
    # Given the arrays "data1" and "data2", returns the
    # Student's "t" and its significance as "prob".
    # Data are assumed to be drawn from populations with
    # the same true variance.

    # Small values of "prob" indicates that the arrays
    # have different means.
    n1 = len(data1)
    n2 = len(data2)

    ave1, var1 = avevar(data1)
    ave2, var2 = avevar(data2)

    # print(ave1, ave2)
    # print(var1, var2)

    # Student's t
    t = (ave1 - ave2) / np.sqrt(var1/n1 + var2/n2)

    df = (var1/n1 + var2/n2)**2 / ((var1/n1)**2 / (n1 - 1) + (var2/n2)**2 / (n2 - 1))
    # significance
    prob = betai(0.5 * df, 0.5, df/(df + t**2))

    return t, prob