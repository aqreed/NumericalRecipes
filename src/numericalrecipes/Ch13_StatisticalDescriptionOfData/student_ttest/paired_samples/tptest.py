import numpy as np
import nr


def tptest(data1, data2):
    # Given the arrays "data1" and "data2" of length "n", returns
    # the Student's "t" for paired data and its significance as "prob".

    # Small values of "prob" indicates that the arrays have different
    # means.

    n1 = len(data1)
    n2 = len(data2)

    if (n1 != n2):
        print("Data arrays must have the same size")
    else:
        n = n1

    ave1, var1 = nr.avevar(data1)
    ave2, var2 = nr.avevar(data2)

    cov = 0.0
    for i in range(n):
        cov = cov + (data1[i] - ave1) * (data2[i] - ave2)

    df = n - 1.0
    cov = cov / df

    # Student's t
    t = (ave1 - ave2) / np.sqrt((var1 + var2 - 2.0 * cov) / n)

    # significance
    prob = nr.betai(0.5 * df, 0.5, df/(df + t**2))

    return t, prob
