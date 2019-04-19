from numba import jit


@jit(nopython=True)
def avevar(data):
    # Given an array "data" of length "n", returns
    # its mean "ave" and its variance "var"
    n = len(data)
    ave, var = 0, 0

    # Mean
    for i in range(n):
        ave = ave + data[i]

    ave = ave / n

    # Variance (of a sample population)
    for i in range(len(data)):
        s = data[i] - ave
        var = var + s**2

    var = var / (n - 1)

    return ave, var
